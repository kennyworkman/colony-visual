"""

colony
~~~~~~
Defines the Colony class.


"""

from cvisual.utils import get_compliment
from cvisual.registry import register
from cvisual.variant import Variant
import logging
import pysam
import os


class ColonyInstantiationError(Exception):
    """An Exception that will be raised if there is a lack of information or an
    error with instantiating a `Colony` class.

    This error will be caught and logged so information is available after a
    large number of colonies are processed.
    """
    pass


class ColonyValidationError(Exception):
    """An Exception that will be raised if there is an issue with validating a
    `Colony` class.

    This error will be caught and logged so information is available after a
    large number of colonies are processed.
    """
    pass


class Base():
    """The Base class for the `Colony` object.

    Stores lists of file paths that the `Colony` class can easily reference to
    find a file compliment.
    """
    bam_list = []
    vcf_list = []

    def __repr__(self):
        return "A Base Class that stores lists of vcf and bam files"


class Colony(Base):
    """An object to represent the genomic information associated with a
    single colony.

    **Can be instantiated with either .bam or .vcf file. It will pull its
    compliment from another list**
    """

    def __init__(self, starter_file, threshold=30, qualbydepth=2,
                 fisherstrand=60, strandoddsratio=3):
        """Assign complimentary .vcf/.bam file, assign coverage score, assign
        validated variants array, and register to the Registry

        :param starter_file: A `.vcf` or `.bam` file path
        :type starter_file: str
        """
        self.threshold = threshold
        self.qualbydepth = qualbydepth
        self.fisherstrand = fisherstrand
        self.strandoddsratio = strandoddsratio
        self.name = os.path.basename(os.path.splitext(starter_file)[0])

        # The idea here is to allow either of the two required .vcf / .bam
        # files to instantiate the Colony. This way if one of them is missing
        # it can be easily logged by catching the custom error.
        if starter_file[-3:] == 'bam':
            self.bam_file = starter_file
        elif starter_file[-3:] == 'vcf':
            self.vcf_file = starter_file
        else:
            raise ColonyInstantiationError("Invalid file type being passed to "
                                           "Colony constructor. Needs to be "
                                           ".bam or .vcf.")

        self.assign_compliment_file(starter_file)

        # Most important pieces of information
        self.coverage_score = self.calculate_coverage_score(
            self.bam_file, self.threshold)
        self.valid_variants = self.validate_variants(self.vcf_file,
                                                     self.qualbydepth,
                                                     self.fisherstrand,
                                                     self.strandoddsratio)
        if self.has_necessary_data():
            # function imported from the cvisual.registry module
            register(self)

    def __repr__(self):
        return self.name

    def assign_compliment_file(self, starter_file):
        """Assigns the missing .vcf / .bam file from the list defined in the
        Base class.

        For example, if the Colony was instantiated with a .bam file, it will
        assign a .vcf file to the `self.vcf_file` attribute.

        :param starter_file: The path for a `.vcf` or `.bam` file
        :param type: str
        :return: None
        """

        assert starter_file[-3:] == 'bam' or starter_file[-3:] == 'vcf', "Some"
        "thing seriously wrong here. Exception should have been caught"
        "in the constructor."

        if starter_file[-3:] == 'bam':
            self.vcf_file = get_compliment(self.vcf_list, starter_file)
        elif starter_file[-3:] == 'vcf':
            self.bam_file = get_compliment(self.bam_list, starter_file)
        else:
            raise ColonyInstantiationError("Need two files to proceed; \
                                           missing one.")

    def calculate_coverage_score(self, bam_file, threshold):
        """Calculate coverage score using pysam from a .bam file.

        The coverage score is calculated by defining a minimum **threshold**
        that will make a residue (single nucleotide read) valid. Anything
        greater than this value will be valid and will be calculated as a
        percentage of the total number of residues.

        :param bam_file: Path to a .bam file
        :type bam_file: str
        :param threshold: Minimum number of reads per residue to be considered
        valid
        :type threshold: int
        :return: Percentage of residues that are greater the given threshold
        :return type: float
        """
        raw_output = pysam.depth(bam_file)

        # NOTE: Probably a better algorithm / implementation here.
        # A grep / awk solution would be better. But perhaps a strictly
        # pythonic algorithm with faster results.
        covered, length = 0, 0
        # The '[:-1]` is to strip trailing newline
        for read in raw_output.split('\n')[:-1]:
            length += 1
            if int(read.split('\t')[2]) >= threshold:
                covered += 1

        # NOTE:
        # This is an expression to get the last residue number
        # raw_output.split( '\n')[-2].split('\t')[2]

        return (covered / length * 100)

        # TODO: if file doesn't exist, abort instantation and log

    def validate_variants(self, vcf_file, qualbydepth, fisherstrand,
                          strandoddsratio):
        """Generate and returns an array of valid variants using pyvcf.

        Uses a variety of technical metrics to evaluate a variant. See this
        [resource](https://gatkforums.broadinstitute.org/gatk/discussion/2806/ho%20wto-apply-hard-filters-to-a-call-set)
        :param vcf_file: A path to a valid `.vcf` file
        :type vcf_file: str
        :param qualbydepth: The variant confidence (QUAL) divided by the depth
        of non-reference samples. A normalized quality threshold that needs to
        be surpassed to validate a read.
        :type qualbydepth: int
        :param fisherstrand: A value that detects strand bias. Greater the
        value, greater the bias.
        :type fisherstrand: int
        :param strandoddsratio: Another method of detecting strand bias.
        :type strandoddsratio: int
        :return: A list of `_pysam.VariantRecord` objects
        """
        vcf_in = pysam.VariantFile(vcf_file)
        valid_variants = []

        for rec in vcf_in.fetch():
            # If the record lacks necessary information, an error is raised that
            # can be caught and logged. A variant is then made anyways.
            try:
                qd = rec.info["QD"]
                fs = rec.info["FS"]
                sor = rec.info["SOR"]

                if ((qd > 2) and
                    (fs < 60) and
                        (sor < 3)):
                    valid_variant = Variant(rec.pos, rec.ref, rec.alts)
                    valid_variants.append(valid_variant)
            except KeyError:
                logging.warning(
                    "Colony {} lacks quality "
                    "information to validate variants. Variants were "
                    "validated anyways.".format(self))

                valid_variant = Variant(rec.pos, rec.ref, rec.alts)
                valid_variants.append(valid_variant)

        return valid_variants

    def is_valid(self, maximum_variants, minimum_coverage):
        """Uses the `coverage_score` and `valid_variants` attributes to
        calculate a "validity" boolean value.

        :param maximum_variants: The maximum number of variants a colony can
        have to be considered valid. The length of the `valid_variants` array.
        :type maximum_variants: int
        :param minimum_coverage: The minimum value of the `coverage_score`
        attribute required to be considered valid.
        :type minimum_coverage: float
        :returns: Boolean True or False
        """
        return self.coverage_score > minimum_coverage and maximum_variants > len(self.valid_variants)

    def has_necessary_data(self):
        """Checks Colony instance for necessary attributes.

        If these attributes are not found, a ColonyInstantiationError is raised
        so that the information can be caught and logged at a higher level.

        :return: `True` if Colony has these attributes, `False` otherwise.
        """
        if self.coverage_score is None:
            raise ColonyValidationError("Colony cannot be validated because \
                                        it is missing a coverage score.")
            return False
        if self.valid_variants is None:
            raise ColonyValidationError("Colony cannot be validated because \
                                        it is missing an empty or non-empty \
                                        variants array.")
            return False
        return True
