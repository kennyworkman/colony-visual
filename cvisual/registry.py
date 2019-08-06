"""

registry
~~~~~~~~
Defines a collection of functions that mimic the behavior of a static Registry
class.

"""

import pandas as pd

colony_list = []


def register(colony):
    """Registers a `Colony` object with the registry module."""
    if colony not in colony_list:
        colony_list.append(colony)


def export_dataframe():
    """Returns a pandas dataframe using all of the colonies currently
    registered with the Registry class
    """
    # Define a Series for each Colony registered
    # Concatenate all of the series into a single DataFrame
    colony_columns = ["Valid", "Variants", "Coverage Score"]
    df = pd.DataFrame(columns=colony_columns)
    for colony in colony_list:
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
