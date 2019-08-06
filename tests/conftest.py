import pytest
from cvisual.utils import get_bam_vcf_files


@pytest.fixture
def dummy_data():
    return get_bam_vcf_files('./tests/dummy_data/')
