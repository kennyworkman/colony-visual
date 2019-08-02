"""

utils
~~~~~
Various utility functions.

"""
from os.path import join, splitext, basename


def enforce_file_compliments(bam_list, vcf_list):
    """All `.bam` files in a given directory must have a complimentary
    `.vcf` counterpart.

    This function enforces that behavior, culling files that don't have a
    match so that incomplete information isn't used to generate a visual.

    :param bam_list: A list of `.bam` absolute paths.
    :type bam_list: list
    :param vcf_list: A list of `.vcf` absolute paths.
    :type vcf_list: list
    :return: None - this function mutates the provided lists.
    """

    for bam_file in bam_list:
        vcf_file = splitext(bam_file)[0] + ".vcf"
        if vcf_file not in vcf_list:
            print(bam_file, " doesn't have an associated .vcf-",
                  vcf_file, "-file.")
            bam_list.remove(bam_file)

    # TODO: Definitely a better way to do this...
    for vcf_file in vcf_list:
        bam_file = splitext(vcf_file)[0] + ".bam"
        if bam_file not in bam_list:
            print(vcf_file, " doesn't have an associated .bam file")
            vcf_list.remove(vcf_file)


def get_compliment(file_list, file):
    """Returns a file path from the provided list that has the same name as the
    file passed as the second arugment.

    :param file_list: A list of paths with the same filetype.
    :type file_list: list
    :param file: A single path with an opposite filetype.
    :type file: str
    :return: A file path
    :return type: str
    """
    compliment = splitext(file)[0]
    for path in file_list:
        if splitext(basename(path))[0] == compliment:
            return path
