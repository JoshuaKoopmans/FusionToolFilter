from modules.collective_script.methods import open_file


class OpenFile:
    def __init__(self, file_in, csv_format=False):
        self._csv_format = csv_format
        self._file_in = file_in

    def open_file(self):
        if self._csv_format is True:
            return open_file(self._file_in, True)
        else:
            return open_file(self._file_in, False)

    # def set_file_in(self, x):
    #     self._file_in = x
    # def get_file_in(self):
    #     return self._file_in
    # def set_tool_name(self):
    #     pass
    # def get_tool_name(self):
    #     return self._tool_name
    # def set_file_in_format(self):
    #     pass
    # def get_file_in_format(self):
    #     return self._file_in_format
# def process_fusion_catcher():
#
#     with open("tests/test_dependencies/final-list_candidate-fusion-genes.tsv", "r") as f:
#         file_content = f.readlines()
#     f.close()
#     return file_content[:4]
