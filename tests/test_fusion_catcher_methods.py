import unittest
from modules.fusioncatcher.methods import check_row_false_positives
from tests.helper import OpenFile

class TestFusionCatcherFilter(unittest.TestCase):
    def test_true_output(self):
        self.assertEqual(check_row_false_positives("banned,cancer,healthy,oncogene"), True)

    def test_false_output(self):
        self.assertEqual(check_row_false_positives("cancer,oncogene"), False)

    def test_processing(self):
        ex = OpenFile("tests/test_dependencies/final-list_candidate-fusion-genes.tsv", False)
        self.assertEqual(ex.open_file()[4].split("\t")[14], "CCCTGAGACTCTGCTGGGGGAGATGGAGGCGAAGACAAGAGAGCTCATTG"
                                                            "*GGAATTTGAAGTAGAAAAACAGACTGCAGAAGAAACGGGGCTTACGCCAT")

if __name__ == '__main__':
    unittest.main()
