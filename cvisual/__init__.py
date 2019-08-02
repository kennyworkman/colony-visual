"""

cvisualize
~~~~~~~~~~
A library for visualizing aligned genomic information.

"""

import os
import glob
import pysam

from cvisual.utils import enforce_file_compliments
from cvisual.colony import Base, Colony


def main(genome_directory):
    """Will generate a pandas dataframe populated with colony information.
    """
    assert isinstance(genome_directory, str), "Directory parameter needs to" \
                                              " a string."

    if not os.path.exists(genome_directory):
        raise FileNotFoundError("The given directory doesn't exist")

    bam_glob = os.path.join(os.path.abspath(genome_directory), "**/*.bam")
    vcf_glob = os.path.join(os.path.abspath(genome_directory), "**/*.vcf")

    bam_files = glob.glob(bam_glob, recursive=True)
    vcf_files = glob.glob(vcf_glob, recursive=True)

    # Essentially culling out .bam or .vcf files that don't have a
    # corresponding match. Eliminates colony parsing with incomplete
    # information.
    enforce_file_compliments(bam_files, vcf_files)

    # Future Colony classes will inherit from the lists defined in the
    # Base class.
    Base.bam_list, Base.vcf_list = bam_files, vcf_files

    # TODO: create and register Colony classes with the Registry class
