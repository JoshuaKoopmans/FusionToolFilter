def create_sf_output(output_file, out_string):
    """
        This function creates an output file and dumps the fusion partners in it.

        :param out_string: string containing all fusion partners in the desired format \
                (e.g. <fusion_partner_1>--<fusion_partner_2>).
        :param output_file: a file to dump he out_string into.
        """
    try:
        with open(output_file, "w") as f_out:
            f_out.write("#FusionName\tJunctionReadCount\tSpanningFragCount\tSpliceType\tLeftGene\t"
                        "LeftBreakpoint\tRightGene\tRightBreakpoint\tJunctionReads\tSpanningFrags\t"
                        "LargeAnchorSupport\tFFPM\tLeftBreakDinuc\tLeftBreakEntropy\tRightBreakDinuc\t"
                        "RightBreakEntropy\tannots\n")
            f_out.write(out_string)
        f_out.close()
    except (FileNotFoundError, IOError) as e:
        print("ERROR: Check output file.", e.args)
        exit(1)


def check_value_above_filter(value, threshold):
    return int(value) >= threshold


def process_star_fusion(file_content, threshold=8):
    out_string = ""
    try:
        for line in file_content:
            if not line.startswith("#"):
                splitted_line = line.split("\t")
                junction_read_count = splitted_line[1]
                spanning_read_count = splitted_line[2]
                if check_value_above_filter(junction_read_count, threshold) and \
                        check_value_above_filter(spanning_read_count, threshold):
                    out_string += line
        return out_string
    except:
        print("ERROR: input file not from selected tool.")
        exit(1)
