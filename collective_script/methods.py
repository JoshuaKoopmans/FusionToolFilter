def check_value_above_filter(value, threshold):
    """
    Returns a boolean to indicate value at or above threshold.

    :param value: integer from a column "*read count".
    :param threshold: threshold for the filtering of these read counts.
    :return: boolean whether integer is equal or greater than threshold.
    """
    return int(value) >= threshold
