import unittest
from modules.collective_script.methods import check_value_above_filter
from modules.arriba.methods import process_arriba
from tests.helper import OpenFile

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script tests the methods used for the processing of Arriba results.
"""


class TestArribaFilter(unittest.TestCase):
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
        ex = OpenFile("tests/test_dependencies/ERR3003530.fusions.tsv", False)
        self.assertEqual(ex.open_file()[3].split("\t")[5].rstrip().split(":")[1], "23295024")

    def test_output(self):
        """
        Test whether the low confidence results are filtered out
        """
        ex = OpenFile("tests/test_dependencies/ERR3003530.fusions.tsv", False)
        expected_count = 8
        count = len(process_arriba(ex.open_file(), False)[0].split("\n"))
        self.assertEqual(count, expected_count)


if __name__ == '__main__':
    unittest.main()
