#!/usr/bin/python3
"""
LFU Cache
"""
from threading import RLock
BaseCaching = __import__('base_caching').BaseCaching


class LFUCache(BaseCaching):
    """
    LFU Cache
    """
    def __init__(self):
        BaseCaching.__init__(self)
        self.__stats = {}
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
            data = self.cache_data.get(key, None)
            if key in self.__stats:
                self.__stats[key] += 1
        return data

    def _balance(self, keyIn):
        """
        Remove Items
        """
        out = None
        if keyIn not in self.__stats:
            if len(self.cache_data) == BaseCaching.MAX_ITEMS:
                out = min(self.__stats, key=self.__stats.get)
                self.cache_data.pop(out)
                self.__stats.pop(out)
        self.__stats[keyIn] = self.__stats.get(keyIn, 0) + 1
        return out

