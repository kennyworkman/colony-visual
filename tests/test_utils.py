from cvisual.utils import *


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

    assert len(vcf_list) == 2, "Files that lack a compliment should be removed"

