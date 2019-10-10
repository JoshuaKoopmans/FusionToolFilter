import unittest
from fusioncatcher.filter_results import check_row_false_positives, process_fusion_catcher


class SolutionProcess:

    def process_fusion_catcher(self):
        with open("test_dependencies/final-list_candidate-fusion-genes.tsv", "r") as f:
            file_content = f.readlines()
        f.close()
        return process_fusion_catcher(file_content)


class TestFusionCatcherFilter(unittest.TestCase):
    def test_true_output(self):
        self.assertEqual(check_row_false_positives("banned,cancer,healthy,oncogene"), True)

    def test_false_output(self):
        self.assertEqual(check_row_false_positives("cancer,oncogene"), False)

    def test_processing(self):
        ex = SolutionProcess()
        self.assertEqual(ex.process_fusion_catcher(), "ABL1--BCR\nBCR--ABL1\nAL133467.2--TCL6\n")


if __name__ == '__main__':
    unittest.main()