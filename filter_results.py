#!/usr/bin/env python

"""
##################################################
Center for molecular and Biomolecular Informatics (CMBI) / RTC Bioinformatics
Author: Joshua Koopmans
Version: 1.0
Email: Joshua.Koopmans@radboudumc.nl
##################################################


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


def check_row_false_positives(row):
    """
    Checks if string in splitted line contains banned terms that indicates possible false positive results.
    
    :param row: splitted line of FusionCatcher output
    :return: boolean whether string contains banned terms.
    """
    if any(term in row for term in banned_term):
        return True
    return False
