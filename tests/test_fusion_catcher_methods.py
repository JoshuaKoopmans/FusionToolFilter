import unittest
from modules.fusioncatcher.methods import check_row_false_positives
from tests.helper import OpenFile

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script tests the methods used for the processing of FusionCatcher results.
"""


class TestFusionCatcherFilter(unittest.TestCase):
    def test_true_output(self):
        """
        Check whether filter works on integer
        """
        self.assertEqual(check_row_false_positives("banned,cancer,healthy,oncogene"), True)

    def test_false_output(self):
        """
        Check whether filter works on integer
        """
        self.assertEqual(check_row_false_positives("cancer,oncogene"), False)

    def test_processing(self):
        """
        Check whether a specific piece of file content matches the expected value
        """
        ex = OpenFile("tests/test_dependencies/final-list_candidate-fusion-genes.tsv", False)
        self.assertEqual(ex.open_file()[4].split("\t")[14], "CCCTGAGACTCTGCTGGGGGAGATGGAGGCGAAGACAAGAGAGCTCATTG"
                                                            "*GGAATTTGAAGTAGAAAAACAGACTGCAGAAGAAACGGGGCTTACGCCAT")


if __name__ == '__main__':
    unittest.main()
