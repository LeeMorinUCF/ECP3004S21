# -*- coding: utf-8 -*-
"""
Created on Mon Mar 15 14:44:02 2021

@author: le279259
"""

from typing import Any

def linear_search(lst: list, value: Any) -> int:
    """... Exactly the same docstring goes here ...
    """

    for i in range(len(lst)):
        if lst[i] == value:
            return i

    return -1

