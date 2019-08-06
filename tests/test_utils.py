from cvisual.utils import (enforce_file_compliments, get_compliment,
                           get_bam_vcf_files)
import os


def test_enforce_file_compliments():
    """Two lists without file compliments should be returned as a single list
    with file compliments
    """
    bam_list = ['a.bam', 'b.bam', 'c.bam']
    vcf_list = ['a.vcf', 'b.vcf', 'c.vcf']

    enforce_file_compliments(bam_list, vcf_list)

    assert len(bam_list) == len(vcf_list), "File compliments" \
        "should be preserved."

    bam_list = ['a.bam', 'b.bam']

    enforce_file_compliments(bam_list, vcf_list)

    assert len(vcf_list) == 2, "Files that lack a compliment should be removed."
    assert vcf_list == ['a.vcf', 'b.vcf'], "Compliment behavior isn't enfoced."

    bam_list = ['a.bam', 'b.bam', 'c.bam']

    enforce_file_compliments(bam_list, vcf_list)

    assert len(bam_list) == 2, "Files that lack a compliment should be removed."
    assert bam_list == ['a.bam', 'b.bam'], "Compliment behavior isn't enfoced."


def test_get_compliments(dummy_data):
    """Should return file path that has the same basename as the provided file
    argument."""

    # Trival test.
    file_list = ['/usr/foo/a.bam', '/random/stuff/c.bam']
    file = '/random/stuff/c.vcf'

    compliment_path = get_compliment(file_list, file)

    assert compliment_path == '/random/stuff/c.bam', "This don't work."

    # More rigorous...
    bam_files, vcf_files = dummy_data
    test_file = bam_files[1]

    assert os.path.splitext(get_compliment(vcf_files, test_file))[
        0] == os.path.splitext(test_file)[0], "Compliment isn't correct."

    # TODO More Testing...


def test_get_bam_vcf_files(dummy_data):
    """Should return accurate lists of .bam/.vcf files from a directory"""

    vcf_files, bam_files = get_bam_vcf_files('./tests/dummy_data')

    assert len(vcf_files) == 8 and len(bam_files) == 8, "Incorrect "
    "functionality."
