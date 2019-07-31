"""

colony
~~~~~~
Defines the Colony class.


"""


class Colony():
    """An object to represent the genomic information associated with a
    single colony.

    **Can be instantiated with either .bam or .vcf file. It will pull its
    compliment from another list**
    """

    def init(self, starter_file):
        """Assign complimentary .vcf/.bam file, assign coverage score, assign
        validated variants array, and register to the Registry
        """
        pass

    def get_compliment_file(self, starter_file):
        """Pull complimentary file and assign from starter_file"""
        pass

    def calculate_coverage_score(self, bam_file):
        """Calculate coverage score using pysam from .bam file"""
        pass

    def validate_variants(self, vcf_file):
        """Generate and assign array of valid variants using pysam or pyvcf."""
        pass

    def register(self):
        """Register this colony to the Registry class"""
        pass
