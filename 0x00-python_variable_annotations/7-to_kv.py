#!/usr/bin/env python3

from typing import Union
from typing import Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Converts a string key and int/float value to a tuple
    """
    return (k, v**2)
