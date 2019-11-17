#!/usr/bin/env python

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script contains the methods used for the processing of JAFFA outputs.
"""

import csv
def create_jaffa_output(output_file, out_string, fusion_inspector_format, out_string_fusion_inspector=""):
    """
        This function creates an output file and dumps the fusion partners in it.

        :param out_string_fusion_inspector:
        :param fusion_inspector_format:
        :param out_string: string containing all fusion partners in the desired format \
                (e.g. <fusion_partner_1>--<fusion_partner_2>).
        :param output_file: a file to dump he out_string into.
        """
    header = "sample\tfusion genes\tchrom1\tbase1\tstrand1\tchrom2\tbase2\tstrand2\tgap (kb)\t" \
                        "spanning pairs\tspanning reads\tinframe\taligns\trearrangement\tcontig\tcontig break\t" \
                        "classification\tknown\n"


    try:
        with open(output_file, "w") as f_out:
            f_out.write(header)
            f_out.write(out_string)
        f_out.close()
        if fusion_inspector_format:
            with open((str(output_file) + ".FI"), "w") as f_out:
                f_out.write("#Fusion_Partners\t" + header)
                f_out.write(out_string_fusion_inspector)
            f_out.close()
    except (FileNotFoundError, IOError) as e:
        print("ERROR: Check output file.", e.args)
        exit(1)


def check_value_above_filter(value, threshold, string=False):
    """
    Returns a boolean to indicate value at or above threshold.

    :param string: whether evaluation must be done on strings, else integers.
    :param value: integer from a column "*read count".
    :param threshold: threshold for the filtering of these read counts.
    :return: boolean whether integer is equal or greater than threshold.
    """
    if string:
        return str(value).strip() == threshold

    return int(value) >= threshold


def process_jaffa(file_content, fusion_inspector_format, confidence_threshold="All", spanning_reads=8):
    """
    This function reads the content of an opened file and filters the rows.

    :param fusion_inspector_format:
    :param file_content: content of input file going to be processed.
    :param confidence_threshold: Confidence level to filter by.
    :param spanning_reads: Amount of spanning reads to filter by.
    :return: String with filtered rows.
    """

    out_string = ""
    out_string_fusion_inspector = ""
    try:
        for line in file_content:
                if not line[0].startswith("sample"):
                    splitted_line = line
                    spanning_read_count = splitted_line[10]
                    confidence = splitted_line[16].replace("\"", "")
                    if check_value_above_filter(confidence, confidence_threshold, string=True) and \
                            check_value_above_filter(spanning_read_count, spanning_reads):
                        out_string += "\t".join([item for item in line])
                        if fusion_inspector_format:
                            genes = splitted_line[1].split(":")
                            left_gene = genes[0]
                            right_gene = genes[1]
                            out_string_fusion_inspector += left_gene + "--" + right_gene + "\t" + "\t".join([item for item in line])
                    elif confidence_threshold == "All":
                        out_string += "\t".join([item for item in line])
                        if fusion_inspector_format:
                            genes = splitted_line[1].split(":")
                            left_gene = genes[0]
                            right_gene = genes[1]
                            out_string_fusion_inspector += left_gene + "--" + right_gene + "\t" + "\t".join([item for item in line])
                    return out_string, out_string_fusion_inspector
    except Exception as e:
        print("ERROR: input file not from tool \'JAFFA\'.")
        print(e)
        exit(1)