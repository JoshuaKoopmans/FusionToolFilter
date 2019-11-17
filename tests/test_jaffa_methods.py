import unittest
from modules.jaffa.methods import check_value_above_filter
from tests.helper import OpenFile

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script tests the methods used for the processing of JAFFA results.
"""


class TestJaffaFilter(unittest.TestCase):
    def test_string_true_output(self):
        """
        Check whether filter works on string
        """
        self.assertEqual(check_value_above_filter("HighConfidence", "HighConfidence", True), True)

    def test_string_false_output(self):
        """
        Check whether filter works on string
        """
        self.assertEqual(check_value_above_filter("HighConfidence", "LowConfidence", True), False)

    def test_int_true_output(self):
        """
        Check whether filter works on integer
        """
        self.assertEqual(check_value_above_filter(100, 99, False), True)

    def test_int_false_output(self):
        """
        Check whether filter works on integer
        """
        self.assertEqual(check_value_above_filter(33, 55, False), False)

    def test_processing(self):
        """
        Check whether a specific piece of file content matches the expected value
        """
        ex = OpenFile("tests/test_dependencies/jaffa_results.csv", True)
        self.assertEqual(int(ex.open_file()[5][14].split(".")[1][2:6]), 4742)


if __name__ == '__main__':
    unittest.main()
