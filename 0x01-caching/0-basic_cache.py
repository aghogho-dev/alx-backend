#!/usr/bin/python3
"""Basic Dictionary"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    Basic Dictionary
    """
    def put(self, key, item):
        """
        Put items
        """
        if key and item:
            self.cache_data.update({key: item})

    def get(self, key):
        """
        Get items
        """
        return self.cache_data.get(key, None)
