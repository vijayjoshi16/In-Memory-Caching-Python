from in_memory_cache import InMemoryCache
from custom_eviction_example import add_random_eviction, get_random_eviction
from sample_workload import run_sample_workload

print("TESTING FIFO CACHE")
cache = InMemoryCache(5, 'FIFO')
run_sample_workload(cache)

print("TESTING LIFO CACHE")
cache = InMemoryCache(5, 'LIFO')
run_sample_workload(cache)

print("TESTING LRU CACHE")
cache = InMemoryCache(5, 'LRU')
run_sample_workload(cache)

print("TESTING CUSTOM EVICTION POLICY CACHE")
cache = InMemoryCache(5, (add_random_eviction, get_random_eviction))
run_sample_workload(cache)