from modules.collective_script.methods import open_file

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This class is used in the unit-testing.

"""


class OpenFile:
    def __init__(self, file_in, csv_format=False):
        self._csv_format = csv_format
        self._file_in = file_in

    def open_file(self):
        """
        Opens a file used to create OpenFile object.

        :return: returns content of opened file.
        """
        if self._csv_format is True:
            return open_file(self._file_in, True)
        else:
            return open_file(self._file_in, False)
