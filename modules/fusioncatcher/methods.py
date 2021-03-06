#!/usr/bin/env python

"""
##################################################
Center for Molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################

This script contains the methods used for the processing of FusionCatcher outputs.
"""

banned_term = ["1000genomes", "banned", "bodymap2", "cacg", "conjoing",
               "cortex", "cta", "ctb", "ctc", "ctd", "distance1000bp",
               "distance100kbp", "distance10kbp", "duplicates",
               "ensembl_fully_interacting", "ensembl_partially_overlapping",
               "ensembl_same_strand", "fragments", "healthy", "hpa", "mt",
               "pair_pseudo_gene", "readthrough", "rp11", "rp", "rrna",
               "short_distance", "similar_reads", "similar_symbols",
               "ucsc_fully_overlapping", "ucsc_same_strand_overlapping"
               ]


def check_row_false_positives(value):
    """
    Checks if string in splitted line contains banned terms that indicates possible false positive results.

    :param value: column "fusion_description" value of splitted line of FusionCatcher output.
    :return: boolean whether string contains banned terms.
    """

    if any(term in value for term in banned_term):
        return True
    return False


def create_fc_output(output_file, out_string, fusion_inspector_format, out_string_fusion_inspector=""):
    """
        This function creates an output file and dumps the fusion partners in it.

        :param fusion_inspector_format:
        :param out_string_fusion_inspector:
        :param out_string: string containing all fusion partners in the desired format \
                (e.g. <fusion_partner_1>--<fusion_partner_2>).
        :param output_file: a file to dump he out_string into.
        """
    header = "Gene_1_symbol(5end_fusion_partner)\tGene_2_symbol(" \
             "3end_fusion_partner)\tFusion_description\tCounts_of_common_mapping_reads\tSpanning_pairs" \
             "\tSpanning_unique_reads\tLongest_anchor_found\tFusion_finding_method\tFusion_point_for_gene_1(" \
             "5end_fusion_partner)\tFusion_point_for_gene_2(3end_fusion_partner)\tGene_1_id(" \
             "5end_fusion_partner)\tGene_2_id(3end_fusion_partner)\tExon_1_id(5end_fusion_partner)\tExon_2_id(" \
             "3end_fusion_partner)\tFusion_sequence\tPredicted_effect\n"

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


def process_fusion_catcher(file_content, fusion_inspector_format):
    """
    This function reads the content of an opened file and extracts and returns fusion partners after filtering.

    :param fusion_inspector_format:
    :param file_content: content of input file going to be processed.
    :return: string containing all fusion partners in the desired format \
            (e.g. <fusion_partner_1>--<fusion_partner_2>).
    """
    out_string = ""
    out_string_fusion_inspector = ""
    try:
        for line in file_content:
            # Parse everything except the header
            if not line.startswith("Gene_1_symbol"):
                splitted_line = line.split("\t")
                # Check if line contains banned terms indicating a false positive
                if not check_row_false_positives(splitted_line[2]):
                    fusion_finding_method = splitted_line[7]
                    # Only take the rows where the fusion finding method is a combination of aligners
                    if ";" in fusion_finding_method:
                        out_string += line
                        # If fusion-inspector argument is set to "yes", generate file content for the additional file
                        if fusion_inspector_format:
                            left_gene = splitted_line[0]
                            right_gene = splitted_line[1]
                            if left_gene + "--" + right_gene not in out_string_fusion_inspector:
                                # Identical output as for no fusion-inspector, except for the first column
                                # (e.g. <fusion-partner-1>--<fusion-partner-2>)
                                out_string_fusion_inspector += str(left_gene).strip() + "--" + str(
                                    right_gene).strip() + "\t" + line

        return out_string, out_string_fusion_inspector
    except:
        print("ERROR: input file not from tool \'FusionCatcher\'.")
        exit(1)
