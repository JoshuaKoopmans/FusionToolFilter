#!/usr/bin/env python

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script contains the methods used for the processing of Arriba outputs.
"""
from filter_fusion_out import check_value_above_filter


def create_arriba_output(output_file, out_string):
    """
        This function creates an output file and dumps the fusion partners in it.

        :param out_string: string containing all fusion partners in the desired format \
                (e.g. <fusion_partner_1>--<fusion_partner_2>).
        :param output_file: a file to dump he out_string into.
        """
    try:
        with open(output_file, "w") as f_out:
            f_out.write("#gene1	gene2\tstrand1(gene/fusion)\tstrand2(gene/fusion)\t"
                        "breakpoint1\tbreakpoint2\tsite1\tsite2\ttype\tdirection1\t"
                        "direction2\tsplit_reads1\tsplit_reads2\tdiscordant_mates\t"
                        "coverage1\tcoverage2\tconfidence\tclosest_genomic_breakpoint1\t"
                        "closest_genomic_breakpoint2\tfilters\tfusion_transcript\t"
                        "reading_frame\tpeptide_sequence\tread_identifiers\n")
            f_out.write(out_string)
        f_out.close()
    except (FileNotFoundError, IOError) as e:
        print("ERROR: Check output file.", e.args)
        exit(1)


def process_arriba(file_content, spanning_threshold=8, junction_threshold=8):
    """
    This function reads the content of an opened file and filters the rows.

    :param file_content: content of input file going to be processed.
    :param spanning_threshold: Amount of spanning reads to filter by.
    :param junction_threshold: Amount of junction reads to filter by.
    :return: String with filtered rows.
    """

    out_string = ""
    try:
        for line in file_content:
            # Parse everything except the header
            if not line.startswith("#"):
                splitted_line = line.split("\t")
                # Extract read counts from line
                spanning_read_count = splitted_line[13]
                # Check if respective read counts are above specified threshold and if so, add to output
                if check_value_above_filter(spanning_read_count, spanning_threshold):
                    out_string += line
        return out_string
    except:
        print("ERROR: input file not from tool \'Arriba\'.")
        exit(1)


"""
#gene1	gene2	strand1(gene/fusion)	strand2(gene/fusion)	breakpoint1	breakpoint2	site1	site2	type	direction1	direction2	split_reads1	split_reads2	discordant_mates	coverage1	coverage2	confidence	closest_genomic_breakpoint1	closest_genomic_breakpoint2	filters	fusion_transcript	reading_frame	peptide_sequence	read_identifiers
BCR	ABL1	+/+	+/+	22:23290413	9:130854064	splice-site	splice-site	translocation	downstream	upstream	17	14	10	128	49	high	0	0	duplicates(6)	0	0	0	0
ABL1	BCR	+/+	+/+	9:130714455	22:23292541	splice-site	splice-site	translocation	downstream	upstream	7	5	3	13	82	high	0	0	duplicates(2)	0	0	0	0
ABL1	BCR	+/+	+/+	9:130714455	22:23295024	splice-site	splice-site	translocation	downstream	upstream	0	2	2	13	103	high	0	0	0	0	0	0	0
ABL1	BCR	+/+	+/+	9:130714455	22:23309424	splice-site	splice-site	translocation	downstream	upstream	0	1	1	13	149	high	0	0	duplicates(2)	0	0	0	0
CR381653.1	CR381670.1	+/+	+/-	21:9327298	21:8859114	splice-site	intron	inversion/3'-3'	downstream	downstream	0	1	2	19	11	high	0	0	0	0	0	0	0

"""
