def add_fifo(cache, capacity, key, value):
    cache[key] = value
    if len(cache) > capacity:
        cache.popitem(last=False)

def add_lifo(cache, capacity, key, value):
    if len(cache) >= capacity:
        cache.popitem(last=True)
    cache[key] = value

def add_lru(cache, capacity, key, value):
    cache[key] = value
    cache.move_to_end(key)
    if len(cache) > capacity:
        cache.popitem(last=False)

def get_fifo(cache, key):
    if key not in cache:
        return None
    else:
        return cache[key]

def get_lifo(cache, key):
    if key not in cache:
        return None
    else:
        return cache[key]

def get_lru(cache, key):
    if key not in cache:
        return None
    else:
        cache.move_to_end(key)
        return cache[key]