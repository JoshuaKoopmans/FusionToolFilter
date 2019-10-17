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


def create_jaffa_output(output_file, out_string):
    """
        This function creates an output file and dumps the fusion partners in it.

        :param out_string: string containing all fusion partners in the desired format \
                (e.g. <fusion_partner_1>--<fusion_partner_2>).
        :param output_file: a file to dump he out_string into.
        """
    try:
        with open(output_file, "w") as f_out:
            f_out.write("transcript\tspanning_pairs\tspanning_reads\tcontig_break\tchrom1\tbase1\tstrand1\tchrom2\t"
                        "base2\tstrand2\tgap\trearrangement\taligns\tinframe\tfusion_genes\tknown\tclassification\n")
            f_out.write(out_string)
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


def process_jaffa(file_content, confidence_threshold="HighConfidence", spanning_reads=8):
    """
    This function reads the content of an opened file and filters the rows.

    :param file_content: content of input file going to be processed.
    :param confidence_threshold: Confidence level to filter by.
    :param spanning_reads: Amount of spanning reads to filter by.
    :return: String with filtered rows.
    """

    out_string = ""
    try:
        for line in file_content:
            if not line.startswith("transcript"):
                splitted_line = line.split("\t")
                spanning_read_count = splitted_line[2]
                confidence = splitted_line[16]
                if check_value_above_filter(confidence, confidence_threshold, string=True) and \
                        check_value_above_filter(spanning_read_count, spanning_reads):
                    out_string += line
        return out_string
    except:
        print("ERROR: input file not from selected tool.")
        exit(1)
