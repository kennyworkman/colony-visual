from cvisual.colony import Base, Colony
from cvisual.registry import register, colony_list, export_dataframe
import os


def test_get_compliment_file(dummy_data):
    """Ensure Colony object is able to get the correct complimentary file."""

    bam_files, vcf_files = dummy_data
    Base.bam_list, Base.vcf_list = bam_files, vcf_files

    random_start = bam_files[0]
    test_colony = Colony(random_start)

    assert os.path.splitext(test_colony.vcf_file)[0] == os.path.splitext(
        test_colony.bam_file)[0], "Function does not provide the "
    "correct file."


def test_calculate_coverage_score(dummy_data):
    """Ensure coverage score is calculated correctly."""

    bam_files, vcf_files = dummy_data
    Base.bam_list, Base.vcf_list = bam_files, vcf_files

    random_start = bam_files[1]
    test_colony = Colony(random_start)

    # TODO: More rigorous testing
    print(test_colony.coverage_score)


def test_validate_variants(dummy_data):
    """Ensure that only valid variants are being returned in the correct
    format"""

    bam_files, vcf_files = dummy_data
    Base.bam_list, Base.vcf_list = bam_files, vcf_files

    random_start = bam_files[2]
    test_colony = Colony(random_start)

    print(random_start)
    print(colony_list)
    print(export_dataframe())

    # TODO: More rigorous testing
    assert len(test_colony.valid_variants) == 1, "Incorrect variant filtering."
