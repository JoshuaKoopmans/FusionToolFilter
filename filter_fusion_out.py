#!/usr/bin/env python
import argparse

from fusioncatcher.methods import create_fc_output, process_fusion_catcher
from starfusion.methods import create_sf_output, process_star_fusion

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script controls the logic of the CLI program. Arguments are created and parsed, 
and depending on the arguments, specific methods are executed.
This script makes use of the python packages "fusioncatcher" and "starfusion". 
"""


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


def main():
    """
    Logic of program. Arguments passed are parsed and assigned to variables.
    Depending on the selected fusion detection tool, some logic specific for that tool is executed.
    """
    args = parse_arguments()
    input_file = args.input
    output_file = args.output
    file_content = open_file(input_file)

    if args.tool == "starfusion":
        read_count_threshold = args.threshold
        out_string = process_star_fusion(file_content, read_count_threshold)
        create_sf_output(output_file, out_string)

    if args.tool == "fusioncatcher":
        out_string = process_fusion_catcher(file_content)
        create_fc_output(output_file, out_string)


def parse_arguments():
    """
    Using argparse, arguments are added for the CLI program.
    Input types, default values, help messages, choices, etc. are declared while adding an argument.
    :return: Object with parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Filter output of either STAR-Fusion or fusionCatcher fusion gene detection tool.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input file in TSV format")
    parser.add_argument("-o", "--output", type=str, required=True, help="Desired output file name")
    parser.add_argument("-t", "--tool", required=True, help="Select tool that generated output file",
                        choices=["starfusion", "fusioncatcher"])
    parser.add_argument("--threshold", type=int, help="Amount of reads to filter by (only starfusion)", default=8)
    args = parser.parse_args()

    # Only if starfusion is the selected tool will you be able to specify a threshold.
    # FusionCatcher output is filtered on terms.
    if args.tool != 'starfusion' and args.threshold != 8:
        parser.error('--threshold can only be set when --tool=starfusion.')
        exit(1)
    return args


main()
