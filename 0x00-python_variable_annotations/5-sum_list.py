#!/usr/bin/env python3


def sum_list(input_list: list[float]) -> float:
    """
    Returns the sum of a list of floats.

    Parameters:
        input_list (list[float]): The list of floats to sum.

    Returns:
        float: The sum of the list of floats.
    """

    total = 0
    for num in input_list:
        total += num
    return total
