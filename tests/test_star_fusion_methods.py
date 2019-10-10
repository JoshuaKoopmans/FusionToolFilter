import unittest
from starfusion.methods import process_star_fusion, check_value_above_filter


class SolutionProcess:

    def process_star_fusion(self):
        with open("test_dependencies/ERR3003549.fusion_predictions.tsv", "r") as f:
            file_content = f.readlines()
        f.close()
        return process_star_fusion(file_content, 20).split("\t")[0]


class TestStarFusionFilter(unittest.TestCase):
    def test_true_output(self):
        self.assertEqual(check_value_above_filter(9, 8), True)

    def test_false_output(self):
        self.assertEqual(check_value_above_filter(5, 8), False)

    def test_processing(self):
        ex = SolutionProcess()
        self.assertEqual(ex.process_star_fusion(), "BCR--ABL1")


if __name__ == '__main__':
    unittest.main()
