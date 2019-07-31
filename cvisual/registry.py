"""

registry
~~~~~~~~
Defines the Registry class.

"""


class Registry():

    def init(self):
        """Initial registry has no colonies."""
        self.colony_list = []

    def register(self, colony):
        """Registers colony (adds object pointer to `colony_list`)"""
        self.colony_list.append(colony)

    def export_dataframe(self):
        """Returns a pandas dataframe using all of the colonies currently
        registered with the Registry class
        """
