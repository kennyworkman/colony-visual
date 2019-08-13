"""

registry
~~~~~~~~
Defines a collection of functions that mimic the behavior of a static Registry
class.

"""

import pandas as pd


class Registry():
    """A Registry class to keep a running list of relevant list of data files
    and colony objects.

    Accessed by the `Colony` object for instantiation information and allows
    downstream export of a pandas DataFrame.
    """

    def __init__(self, bam_list, vcf_list):
        """ TODO: DOCS
        """
        self.bam_list = bam_list
        self.vcf_list = vcf_list
        self.colony_list = []

    def register(self, colony):
        """Registers a `Colony` object with the registry module."""
        if colony not in self.colony_list:
            self.colony_list.append(colony)

    def export_dataframe(self):
        """Returns a pandas dataframe using all of the colonies currently
        registered with the Registry class
        """
        # Define a Series for each Colony registered
        # Concatenate all of the series into a single DataFrame
        colony_columns = ["Valid", "Variants", "Coverage Score"]
        df = pd.DataFrame(columns=colony_columns)
        for colony in self.colony_list:
            # colony.name is used to organize the Series in the index of the
            # Dataframe
            colony_series = pd.Series(name=colony.name, data={
                "Valid": colony.is_valid(
                    maximum_variants=3,
                    minimum_coverage=90),
                "Variants": colony.valid_variants,
                "Coverage Score": colony.coverage_score},
                index=colony_columns)
            df = df.append(colony_series)
        return df
