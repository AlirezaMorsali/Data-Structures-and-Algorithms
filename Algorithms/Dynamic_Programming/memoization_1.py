from time import perf_counter, sleep
from functools import lru_cache

run_times = 5


def slow_function(n):
    sleep(.5)
    return n


start_time = perf_counter()
for _ in range(run_times):
    slow_function(35)
print(
    f"Time to run slow function {run_times} times:{perf_counter()-start_time}")


@lru_cache
def another_slow_function(n):
    sleep(.5)
    return n


start_time = perf_counter()
for _ in range(run_times):
    another_slow_function(35)
print(
    f"Time to run python caching slow function {run_times} times:{perf_counter()-start_time}")
print(another_slow_function.cache_info())

res = {}


def cached_slow(n):
    if n in res:
        return res[n]
    else:
        res[n] = slow_function(n)
        return res[n]


start_time = perf_counter()
for _ in range(run_times):
    cached_slow(35)
print(
    f"Time to run globally cached slow function {run_times} times:{perf_counter()-start_time}")


def clean_cached():
    res = {}

    def internal_cached_slow(n):
        if n in res:
            return res[n]
        else:
            res[n] = slow_function(n)
            return res[n]

    return internal_cached_slow


start_time = perf_counter()
clc = clean_cached()
for _ in range(run_times):
    clc(35)
print(
    f"Time to run closure cached function {run_times} times:{perf_counter()-start_time}")
