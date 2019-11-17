import csv


def open_file(file_name, csv_format=False):
    """
    This function opens a desired file and returns the content.

    :param csv_format:
    :param file_name: name of input file going to be processed.
    :return: content of the opened file.
    """
    try:

        with open(file_name, "r") as f:
            if csv_format:
                reader = csv.reader(f, delimiter=',', dialect="excel")
                content = []
                for row_list in reader:
                    content.append([item.rstrip() for item in row_list])
            else:
                content = f.readlines()
        f.close()
        return content
    except (FileNotFoundError, IOError) as e:
        print("ERROR: Check input file.", e.args)
        exit(1)


def check_value_above_filter(value, threshold):
    """
    Returns a boolean to indicate value at or above threshold.

    :param value: integer from a column "*read count".
    :param threshold: threshold for the filtering of these read counts.
    :return: boolean whether integer is equal or greater than threshold.
    """
    return int(value) >= threshold