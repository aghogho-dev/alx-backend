#!/usr/bin/python3
"""FIFO Cache"""
from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache
    """
    def __init__(self):
        """
        Instantiate
        """
        BaseCaching.__init__(self)
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """
        Put items
        """
        if key and item:
            out = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if out:
                print("DISCARD: {}".format(out))

    def get(self, key):
        """
        Get items
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """
        Remove the oldest
        """
        out = None
        with self.__rlock:
            if keyIn not in self.__keys:
                n = len(self.__keys)
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    out = self.__keys.pop(0)
                    self.cache_data.pop(out)
                self.__keys.insert(n, keyIn)
        return out
