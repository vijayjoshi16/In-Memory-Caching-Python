from collections import OrderedDict
from threading import Lock
from standard_evictions import *

class InMemoryCache:
    def __init__(self, capacity, evict_policy):
        self.capacity = capacity
        self.evict_policy = evict_policy
        self.cache = OrderedDict()
        self.lock = Lock()
        self.evict_policy_fns = {
            'FIFO': (add_fifo, get_fifo),
            'LIFO': (add_lifo, get_lifo),
            'LRU': (add_lru, get_lru)
        }
    
    def add(self, key, value):
        with self.lock:
            if self.evict_policy in self.evict_policy_fns:
                self.evict_policy_fns[self.evict_policy][0](
                    self.cache, self.capacity, key, value
                )
            elif isinstance(self.evict_policy, tuple) and callable(self.evict_policy[0]):
                self.evict_policy[0](
                    self.cache, self.capacity, key, value
                )
            else:
                raise ValueError('Invalid eviction policy')

    def get(self, key):
        with self.lock:
            if self.evict_policy in self.evict_policy_fns:
                return self.evict_policy_fns[self.evict_policy][1](
                    self.cache, key
                )
            elif isinstance(self.evict_policy, tuple) and callable(self.evict_policy[1]):
                self.evict_policy[1](
                    self.cache, key
                )
            else:
                raise ValueError('Invalid eviction policy')
