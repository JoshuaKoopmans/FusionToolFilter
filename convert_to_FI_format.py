#!/usr/bin/env python3

"""
##################################################
Center for molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script converts the FusionCatcher fusion detection tool output into the required input \
for the FusionInspector fusion validation tool.

e.g.    Col1 | Col2  ->   Col1
        ABL1 | BCR   ->   ABL1--BCR
"""

import sys


def open_file(file_name):
    """
    This function opens a desired file and returns the content.

    :param file_name: name of input file going to be processed.
    :return: content of the opened file.
    """
    try:
        with open(file_name, "r") as f:
            content = f.readlines()
        f.close()
        return content
    except (FileNotFoundError, IOError) as e:
        print("ERROR: Check input file.", e.args)
        exit(1)

def process_content(file_name):
    """
    This function reads the content of an opened file and extracts and returns fusion partners.

    :param file_name: name of input file going to be processed.
    :return: string containing all fusion partners in the desired format \
            (e.g. <fusion_partner_1>--<fusion_partner_2>).
    """
    out_string = ""
    file_content = open_file(file_name)
    for line in file_content:
        if not line.startswith("Gene_1_symbol"):
            splitted_line = line.split("\t")
            left_gene = splitted_line[0]
            right_gene = splitted_line[1]
            if left_gene + "--" + right_gene not in out_string:
                out_string += left_gene + "--" + right_gene + "\n"
    return out_string


def create_output_file(out_string, output_file):
    """
    This function creates an output file and dumps the fusion partners in it.

    :param out_string: string containing all fusion partners in the desired format \
            (e.g. <fusion_partner_1>--<fusion_partner_2>).
    :param output_file: a file to dump he out_string into.
    """
    try:
        with open(output_file, "w") as f_out:
            f_out.write("Fusion_Partners\n")
            f_out.write(out_string)
        f_out.close()
    except (FileNotFoundError, IOError) as e:
        print("ERROR: Check output file.", e.args)
        exit(1)

def main():
    """
    Run functions in logical order.
    """
    if len(sys.argv) <= 1:
        print('script.py <input_file> <output_file>')
        exit(1)
    try:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        out_string = process_content(input_file)
        create_output_file(out_string, output_file)


    except IndexError:
        print("ERROR: 2 arguments expected" + "(" + str(len(sys.argv)-1) + " given)")
        exit(1)

if __name__ == "__main__":
    main()


