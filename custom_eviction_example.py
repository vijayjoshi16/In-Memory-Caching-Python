from random import randrange

def add_random_eviction(cache, capacity, key, value):
    if len(cache) >= capacity:
        random_index = randrange(0, capacity)
        cache.pop(list(cache.keys())[random_index])
    cache[key] = value

def get_random_eviction(cache, key):
    if key not in cache:
        return None
    else:
        return cache[key]