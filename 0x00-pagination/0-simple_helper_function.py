#!/usr/bin/env python3
"""Simple helper function."""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Simple helper function
    """
    nextIndex = page * page_size
    return nextIndex - page_size, nextIndex
