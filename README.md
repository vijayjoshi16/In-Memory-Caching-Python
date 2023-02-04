## Problem Statement:

Design and Implement an in-memory caching library for general use

## Must Have

1. Support for multiple Standard Eviction Policies ( FIFO, LRU, LIFO )
2. Support to add custom eviction policies

## Good To Have
1. Thread saftey

## Description about various files:

1. in_memory_cache.py: Class for the in memory cache. You can use this class for initializing the objects for your cache and it takes the cache capacity and eviction policy in arguments. Pass the eviction policy string(FIFO, LRU, LIFO) in case of standart eviction policies. In case of custom eviction policies, pass a tuple consisting of 2 functions for add and get elements from cache respectively. The InMemoryCache class consists of member functions add and get to call the eviction policy specific add and get functions
2. standard_evictions.py: It consists of the add and get functions for standard eviction policies
3. custom_eviction_example: It consists of the add and get functions for any custom eviction policy(random eviction is used in this example)
4. sample_app.py: Entry point to our code to test different types of cache eviction policies
5. sample_workload.py: Consists of a set of add and get queries for the cache

## How to run
1. Clone the project
2. cd to the cloned In-Memory-Caching-Python directory
3. Check for py --version(In my case it is Python 3.10.1)
4. Run sample_app.py: py sample_app.py
