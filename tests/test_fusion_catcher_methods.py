import unittest
from modules.fusioncatcher.methods import check_row_false_positives, process_fusion_catcher


class SolutionProcess:

    def process_fusion_catcher(self):
        with open("tests/test_dependencies/final-list_candidate-fusion-genes.tsv", "r") as f:
            file_content = f.readlines()
        f.close()
        return process_fusion_catcher(file_content).split("\t")[:4]


class TestFusionCatcherFilter(unittest.TestCase):
    def test_true_output(self):
        self.assertEqual(check_row_false_positives("banned,cancer,healthy,oncogene"), True)

    def test_false_output(self):
        self.assertEqual(check_row_false_positives("cancer,oncogene"), False)

    def test_processing(self):
        ex = SolutionProcess()
        self.assertEqual(ex.process_fusion_catcher(), ['ABL1--BCR', 'ABL1', 'BCR',
                                                       'known,oncogene,chimerdb2,cgp,ticdb,tcga,cell_lines,chimerdb3kb,chimerdb3pub,chimerdb3seq,cancer,tumor,m401,tcga-cancer,tcga2,mitelman,exon-exon,reciprocal'])


if __name__ == '__main__':
    unittest.main()
