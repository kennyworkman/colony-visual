"""

cvisualize
~~~~~~~~~~
A library for visualizing aligned genomic information.

"""
import logging
from cvisual.utils import get_bam_vcf_files, enforce_file_compliments
from cvisual.colony import (Base, Colony, ColonyInstantiationError,
                            ColonyValidationError)
from cvisual.registry import colony_list, export_dataframe


def main(genome_directory):
    """Script that generates a dataframe and logs errors."""

    logging.basicConfig(filename='cvisual.log', level=logging.INFO)
    # Handler writes messages to sys.stderr in addition to writing to a log
    # file. Displays in terminal output
    console = logging.StreamHandler()
    logging.getLogger().addHandler(console)

    generate_dataframe(genome_directory)

    print(export_dataframe())
    print(colony_list)


def generate_dataframe(genome_directory):
    """Will generate a pandas dataframe populated with colony information.

    TODO: more documentation

    :param genome_directory: Path to the directory of interest containing .vcf
    and .bam files
    :type genome_directory: str
    :returns: A `DataFrame` from the pandas library
    """

    assert isinstance(genome_directory, str), "Directory parameter needs to" \
                                              " a string."

    bam_files, vcf_files = get_bam_vcf_files(genome_directory)

    # Essentially culling out .bam or .vcf files that don't have a
    # corresponding match. Eliminates colony parsing with incomplete
    # information.
    enforce_file_compliments(bam_files, vcf_files)

    # Future Colony classes will inherit from the lists defined in the
    # Base class.
    Base.bam_list, Base.vcf_list = bam_files, vcf_files

    for bam_file in bam_files:
        try:
            Colony(bam_file)
        except (ColonyValidationError, ColonyInstantiationError) as e:
            logging.warning(e)

    return export_dataframe()


if __name__ == "__main__":
    main('/Users/kenny/projects/colony-visual/mountfolder')
