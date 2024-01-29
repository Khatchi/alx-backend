#!/usr/bin/env python3
"""a func module that defines index_range"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int]:
    """returns a tuple of size two containing a start index and an end index"""
    return (page_size * (page - 1), page_size * page)
