"""

utils
~~~~~
Various utility functions.

"""
from os.path import join, splitext


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
