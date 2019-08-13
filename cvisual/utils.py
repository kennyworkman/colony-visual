"""

utils
~~~~~
Various utility functions.

"""
import os
import glob


def get_bam_vcf_files(directory, username=None):
    """Return a list of .vcf paths and .bam paths from a valid directory

    :param directory: Valid path to a DIVA style directory
    :type directory: str
    :param username: Username used to filter files
    :type username: str
    :return: A list of `.vcf` files and a list of `.bam` file
    :return type: list
    """
    if not os.path.exists(directory):
        raise FileNotFoundError("The given directory doesn't exist")

    # Print empty string if string format variable is None
    # https://stackoverflow.com/questions/33271212/make-string-format-ignore-none
    bam_glob = os.path.join(os.path.abspath(directory),
                            "**/*{}*.bam".format("" if username is None
                                                 else username))
    vcf_glob = os.path.join(os.path.abspath(directory),
                            "**/*{}*.vcf".format("" if username is None
                                                 else username))

    bam_files = glob.glob(bam_glob, recursive=True)
    vcf_files = glob.glob(vcf_glob, recursive=True)

    return bam_files, vcf_files


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
        vcf_file = os.path.splitext(bam_file)[0] + ".vcf"
        if vcf_file not in vcf_list:
            print(bam_file, "doesn't have an associated .vcf file (",
                  vcf_file, ").")
            bam_list.remove(bam_file)

    # TODO: Definitely a better way to do this...
    for vcf_file in vcf_list:
        bam_file = os.path.splitext(vcf_file)[0] + ".bam"
        if bam_file not in bam_list:
            print(vcf_file, "doesn't have an associated .bam file (",
                  bam_file, ").")
            vcf_list.remove(vcf_file)


def get_compliment(file_list, file):
    """Returns a file path from the provided list that has the same name as the
    file passed as the second arugment.

    :param file_list: A list of paths with the same filetype.
    :type file_list: list
    :param file: A single path with an opposite filetype.
    :type file: str
    :return: A file path
    :return type: str, None if nothing found
    """
    compliment = os.path.splitext(file)[0]
    for path in file_list:
        if os.path.splitext(path)[0] == compliment:
            return path
