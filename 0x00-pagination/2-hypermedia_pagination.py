#!/usr/bin/env python3
"""Simple pagination."""
import csv
import math
from typing import Dict, List, Tuple, Union


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    @staticmethod
    def index_range(page: int, page_size: int) -> Tuple[int, int]:
        """
        Index range
        """
        nextIndex = page * page_size
        return nextIndex - page_size, nextIndex

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page
        """
        assert type(page) == type(page_size) == int
        assert page > 0 and page_size > 0
        firstIndex, lastIndex = self.index_range(page, page_size)
        return self.dataset()[firstIndex:lastIndex]

    def get_hyper(self, page: int, 
            page_size: int) -> Dict[str, Union[int, List[List], None]]:
        """
        Get hyper
        """
        data = self.get_page(page, page_size)
        n_rows = len(self.dataset())
        prevPage = page - 1 if page > 1 else None
        nextPage = page + 1
        if self.index_range(page, page_size)[1] >= n_rows:
            nextPage = None
        totalPages = n_rows / page_size
        if totalPages % 1 != 0:
            totalPages += 1
        return {
                'page_size': len(data), 'page': page,
                'data': data, 'next_page': nextPage,
            'prev_page': prevPage, 'total_pages': int(totalPages)
                }
