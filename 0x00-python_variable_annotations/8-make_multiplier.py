#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Returns a function that multiplies a float by multiplier.

    Args:
        multiplier (float): The multiplier to multiply the float by.

    Returns:
        Callable[[float], float]: It multiplies a float by multiplier.
    """
    def multiply(num: float) -> float:
        """
        Multiplies a float by multiplier.

        Args:
            num (float): The float to multiply.

        Returns:
            float: The result of multiplying num by multiplier.
        """
        return num * multiplier
    return multiply
