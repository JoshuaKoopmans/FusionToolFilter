import unittest
from modules.starfusion.methods import check_value_above_filter
from tests.helper import OpenFile

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script tests the methods used for the processing of STAR-Fusion results.
"""


class TestStarFusionFilter(unittest.TestCase):
    def test_true_output(self):
        """
        Check whether filter works on integer
        """
        self.assertEqual(check_value_above_filter(9, 8), True)

    def test_false_output(self):
        """
        Check whether filter works on integer
        """
        self.assertEqual(check_value_above_filter(5, 8), False)

    def test_processing(self):
        """
        Check whether a specific piece of file content matches the expected value
        """
        ex = OpenFile("tests/test_dependencies/ERR3003549.fusion_predictions.tsv", False)
        self.assertEqual(ex.open_file()[2].split("\t")[8], "ERR3003549.35514118,ERR3003549.26593596,ERR3003549.4876846,"
                                                           "ERR3003549.132222,ERR3003549.23880496,ERR3003549.1459710,"
                                                           "ERR3003549.34271762,ERR3003549.23877880,ERR3003549.31002074,"
                                                           "ERR3003549.35767423,ERR3003549.34871132,ERR3003549.23311128,"
                                                           "ERR3003549.2510524,ERR3003549.26239911,ERR3003549.24106263,"
                                                           "ERR3003549.13747215,ERR3003549.1157243,ERR3003549.35462450,"
                                                           "ERR3003549.11226777,ERR3003549.7469243,ERR3003549.13564551,"
                                                           "ERR3003549.37646628,ERR3003549.21763831,ERR3003549.12397896,"
                                                           "ERR3003549.24734818,ERR3003549.6427191,ERR3003549.14293731,"
                                                           "ERR3003549.22490457,ERR3003549.41394459,ERR3003549.23932326,"
                                                           "ERR3003549.27532262,ERR3003549.957032,ERR3003549.18054556,"
                                                           "ERR3003549.5056587,ERR3003549.20106936,ERR3003549.20813627,"
                                                           "ERR3003549.34020876,ERR3003549.4052860,ERR3003549.10823571,"
                                                           "ERR3003549.27970515,ERR3003549.38559607,ERR3003549.19660361,"
                                                           "ERR3003549.10101131,ERR3003549.27728776,ERR3003549.30418961,"
                                                           "ERR3003549.34400349,ERR3003549.42191939,ERR3003549.40548193,"
                                                           "ERR3003549.41738925,ERR3003549.33348710,ERR3003549.16904117,"
                                                           "ERR3003549.34350166,ERR3003549.24335298,ERR3003549.17813454,"
                                                           "ERR3003549.11154232,ERR3003549.33578004,ERR3003549.37972998,"
                                                           "ERR3003549.1386700")


if __name__ == '__main__':
    unittest.main()
