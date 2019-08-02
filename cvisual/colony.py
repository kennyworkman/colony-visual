"""

colony
~~~~~~
Defines the Colony class.


"""

from cvisual.utils import get_compliment


class Base():
    """The Base class for the `Colony` object.

    Stores lists of file paths that the `Colony` class can easily reference to
    find a file compliment.
    """
    bam_list = []
    vcf_list = []

    def __repr__(self):
        return "Base object with {} bam files, and {} vcf "
        "files".format(len(self.bam_list), len(self.vcf_list))


class Colony(Base):
    """An object to represent the genomic information associated with a
    single colony.

    **Can be instantiated with either .bam or .vcf file. It will pull its
    compliment from another list**
    """

    def __init__(self, starter_file):
        """Assign complimentary .vcf/.bam file, assign coverage score, assign
        validated variants array, and register to the Registry
        """
        if starter_file[-3:] == 'bam':
            self.bam_file = starter_file
        elif starter_file[-3:] == 'vcf':
            self.vcf_file = starter_file
        else:
            raise TypeError("Invalid file type being passed to Colony"
                            "constructor. Needs to be .bam or .vcf.")

        self.get_compliment_file(starter_file)

    def get_compliment_file(self, starter_file):
        """Pull complimentary file and assign from starter_file"""

        assert starter_file[-3:] == 'bam' or starter_file[-3:] == 'vcf', "Some"
        "thing seriously wrong here. Exception should have been caught"
        "in the constructor."

        if starter_file[-3:] == 'bam':
            self.vcf_file = get_compliment(self.vcf_list, starter_file)
        elif starter_file[-3:] == 'vcf':
            self.bam_file = get_compliment(self.bam_list, starter_file)
        else:
            raise FatalError("Need two files to proceed, missing one")
            # TODO: abort instantiation and log the failed colony because of
            # lack of information...
            # Need both files to proceed so this should be a fatal error

    def calculate_coverage_score(self, bam_file):
        """Calculate coverage score using pysam from .bam file"""
        pass

    def validate_variants(self, vcf_file):
        """Generate and assign array of valid variants using pysam or pyvcf."""
        pass

    def register(self):
        """Register this colony to the Registry class"""
        pass
