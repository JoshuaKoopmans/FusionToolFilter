#!/usr/bin/env python
import argparse

from collective_script.methods import open_file
from fusioncatcher.methods import create_fc_output, process_fusion_catcher
from starfusion.methods import create_sf_output, process_star_fusion
from jaffa.methods import create_jaffa_output, process_jaffa
from arriba.methods import create_arriba_output, process_arriba

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



def main():
    """
    Logic of program. Arguments passed are parsed and assigned to variables.
    Depending on the selected fusion detection tool, some logic specific for that tool is executed.
    """
    args = parse_arguments()
    input_file = args.input
    output_file = args.output
    file_content = open_file(input_file)
    fusion_inspector_format = False

    if args.fusion_inspector == "yes":
        fusion_inspector_format = True

    if args.tool == "starfusion":
        junction_threshold = args.threshold_junction
        spanning_threshold = args.threshold_spanning
        out_string = process_star_fusion(file_content, spanning_threshold, junction_threshold)
        create_sf_output(output_file, out_string)

    if args.tool == "fusioncatcher":
        out_string, out_string_fusion_inspector = process_fusion_catcher(file_content, fusion_inspector_format)
        create_fc_output(output_file, out_string, fusion_inspector_format, out_string_fusion_inspector)

    if args.tool == "jaffa":
        spanning_threshold = args.threshold_spanning
        # confidence_threshold = args.threshold_confidence
        out_string = process_jaffa(file_content, spanning_threshold)
        create_jaffa_output(output_file, out_string)

    if args.tool == "arriba":
        junction_threshold = args.threshold_junction
        spanning_threshold = args.threshold_spanning
        out_string, out_string_fusion_inspector = process_arriba(file_content, spanning_threshold, junction_threshold)
        create_arriba_output(output_file, out_string, fusion_inspector_format, out_string_fusion_inspector)

def parse_arguments():
    """
    Using argparse, arguments are added for the CLI program.
    Input types, default values, help messages, choices, etc. are declared while adding an argument.
    :return: Object with parsed arguments.
    """
    parser = argparse.ArgumentParser(
        description="Filter output of either STAR-Fusion or fusionCatcher fusion gene detection tool.")
    parser.add_argument("-i", "--input", type=str, required=True, help="Input file")
    parser.add_argument("-o", "--output", type=str, required=True, help="Desired output file name")
    parser.add_argument("-t", "--tool", type=str, required=True, help="Select tool that generated output file",
                        choices=["starfusion", "fusioncatcher", "jaffa", "arriba"])
    parser.add_argument("--threshold-junction", type=int,
                        help="Amount of junction reads to filter by (only starfusion & arriba)",
                        default=8)
    parser.add_argument("--threshold-spanning", type=int, help="Amount of spanning frag reads to filter by "
                                                               "(only starfusion & arriba)",
                        default=8)
    parser.add_argument("--threshold-confidence", type=str, help="Confidence level to filter by (only jaffa)",
                        default="HighConfidence", choices=["HighConfidence", "MediumConfidence", "LowConfidence"])
    parser.add_argument("--fusion-inspector", type=str, help="Additional filtered file with the first column formatted"
                                                             " for FusionInspector",
                        choices=("yes", "no"), default="no")
    args = parser.parse_args()

    # Only if starfusion or jaffa or arriba is the selected tool will you be able to specify a threshold for spanning reads.
    # Only is starfusion or arriba is the selected tool will you be able to specify a threshold for junction reads.
    # Only is jaffa is the selected tool will you be able to specify a threshold confidence.
    # FusionCatcher output is filtered on terms.
    if (args.tool not in ["starfusion", "arriba"]) and args.threshold_junction != 8:
        parser.error('--threshold-junction can only be set when --tool=starfusion or --tool=arriba.')
        exit(1)
    if (args.tool not in ["starfusion", "jaffa", "arriba"]) and args.threshold_spanning != 8:
        parser.error('--threshold-spanning can only be set when --tool=starfusion or --tool=jaffa or --tool=arriba.')
        exit(1)
    # if args.tool != 'jaffa' and args.threshold_confidence != "HighConfidence":
    #     parser.error('--threshold-confidence can only be set when --tool=jaffa.')
    #     exit(1)
    return args


main()
