from time import perf_counter
from functools import cache

n = 35


def dumb_fib(n):
    if n < 2:
        return n
    else:
        return dumb_fib(n-1) + dumb_fib(n-2)


start_time = perf_counter()
dumb_fib(n)
print(f"Time to run dumb_fib{n}: {perf_counter()-start_time}")


@cache
def p_fib(n):
    if n < 2:
        return n
    else:
        return p_fib(n-1) + p_fib(n-2)


start_time = perf_counter()
p_fib(n)
print(f"Time to run p_fib{n}: {perf_counter()-start_time}")


def fib(n):
    def go(n, x, y):
        if n == 0:
            return y
        if n == 1:
            return x
        else:
            return go(n-1, x+y, x)
    return go(n, 1, 0)


for i in range(10):
    print(f"p_fib({i}): {p_fib(i)}")
    print(f"fib({i}): {fib(i)}")
