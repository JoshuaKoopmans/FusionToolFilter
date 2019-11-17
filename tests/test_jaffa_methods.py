import unittest
from modules.jaffa.methods import check_value_above_filter
from tests.helper import OpenFile


class TestJaffaFilter(unittest.TestCase):
    def test_string_true_output(self):
        self.assertEqual(check_value_above_filter("HighConfidence", "HighConfidence", True), True)

    def test_string_false_output(self):
        self.assertEqual(check_value_above_filter("HighConfidence", "LowConfidence", True), False)

    def test_int_true_output(self):
        self.assertEqual(check_value_above_filter(100, 99, False), True)

    def test_int_false_output(self):
        self.assertEqual(check_value_above_filter(33, 55, False), False)

    def test_processing(self):
        ex = OpenFile("tests/test_dependencies/jaffa_results.csv", True)
        self.assertEqual(int(ex.open_file()[5][14].split(".")[1][2:6]), 4742)


if __name__ == '__main__':
    unittest.main()
