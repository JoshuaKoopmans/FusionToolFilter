#!/usr/bin/env python

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################


"""

import sys
import pandas as pd
import numpy as np


def create_dataframes(file_left, file_right, delimiter, header):
    # Create a DataFrames
    df_left = pd.read_csv(file_left, sep=delimiter, header=header)
    df_right = pd.read_csv(file_right, sep=delimiter, header=header)

    return df_left, df_right


def get_intersection(df_left, df_right):
    intersected_df = pd.merge(df_left, df_right, how='inner')
    return intersected_df


def create_out_file(intersected_df):
    return pd.DataFrame.to_csv(intersected_df, sep="\t")


def main():
    """
    Run functions in logical order.
    """
    if len(sys.argv) <= 1:
        print('script.py <input_file_1> <input_file_2> <output_file>')
        exit(1)
    try:
        fusion_out_file_1 = sys.argv[1]
        fusion_out_file_2 = sys.argv[2]
        intersection_out_file = sys.argv[3]
        # out_string = process_content(input_file)
        # create_output_file(out_string, output_file)


    except IndexError:
        print("ERROR: 3 arguments expected" + "(" + str(len(sys.argv) - 1) + " given)")
        exit(1)


if __name__ == "__main__":
    main()
