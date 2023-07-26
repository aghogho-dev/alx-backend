#!/usr/bin/python3
"""
LIFO Caching
"""
from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO Cache
    """
    def __init__(self):
        """
        Initialize
        """
        BaseCaching.__init__(self)
        self.__keys = []
        self.__rlock = RLock()

    def put(self, key, item):
        """
        Put Items
        """
        if key and item:
            out = self._balance(key)
            with self.__rlock:
                self.cache_data.update({key: item})
            if out:
                print("DISCARD: {}".format(out))

    def get(self, key):
        """
        Get Items
        """
        with self.__rlock:
            return self.cache_data.get(key, None)

    def _balance(self, keyIn):
        """
        Remove Items
        """
        out = None
        with self.__rlock:
            n = len(self.__keys)
            if keyIn not in self.__keys:
                if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                    out = self.__keys.pop(n - 1)
                    self.cache_data.pop(out)
            else:
                self.__keys.remove(keyIn)
            self.__keys.insert(n, keyIn)
        return out
