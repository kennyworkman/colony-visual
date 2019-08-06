"""

variant
~~~~~~~
Defines the Variant class.

"""


class Variant():
    """A data abstraction for a single variant call from a .vcf file.

    Easily extract relevant information, for export to a pandas DataFrame
    or other downstream application, with get methods

    :param positon: Nucleotide position
    :type position: int
    :param reference: What the nuceotide should be
    :type reference: str
    :param alternates: Reads other than the expected reference
    :type alternates: tuple
    """

    def __init__(self, position, reference, alternates):
        """TODO
        """
        self.position = position
        self.reference = reference
        self.alternates = alternates

    def get_formatted(self):
        return "Position: {}, Reference: {}, Alternate: " \
            "{}".format(self.position, self.reference, self.alternates)

    def __repr__(self):
        return self.get_formatted()
