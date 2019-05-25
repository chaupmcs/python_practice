import time
from functools import lru_cache


def fibonacci_recursion(n):
    """ calc fibonacci recursively """
    if (n == 1) or (n == 2):
        return 1

    return fibonacci_recursion(n-1) + fibonacci_recursion(n-2)


@lru_cache() # LRU (least recently used) cache, read more https://pymi.vn/blog/memoization/
def fibonacci_recursion_lru(n):
    """ calc fibonacci recursively """
    if (n == 1) or (n == 2):
        return 1

    return fibonacci_recursion_lru(n-1) + fibonacci_recursion_lru(n-2)


def fibonacci_memoization_helper(n, cache):

    if n in cache:
        return cache[n]
    else:
        cache[n] = fibonacci_memoization_helper(n-1, cache) + fibonacci_memoization_helper(n-2, cache)
        return cache[n]

def fibonacci_memoization(n):
    cache = dict()
    cache[1] = 1
    cache[2] = 1

    return fibonacci_memoization_helper(n, cache)



def calc_time(func, n):
    start_time = time.time()
    res = func(n)
    end_time = time.time()
    dt = end_time - start_time
    message = "The result is {res}; time execution is {dt}"
    print(message.format(res = res, dt = dt))


n = 80

calc_time(fibonacci_memoization, n)
calc_time(fibonacci_recursion_lru, n)


