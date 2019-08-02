from cvisual.utils import enforce_file_compliments, get_compliment


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


def test_get_compliments():
    """Should return file path that has the same basename as the provided file
    argument."""

    file_list = ['/usr/foo/a.bam', '/random/stuff/c.bam']
    file = 'c.vcf'

    compliment_path = get_compliment(file_list, file)

    assert compliment_path == '/random/stuff/c.bam', "This don't work."
