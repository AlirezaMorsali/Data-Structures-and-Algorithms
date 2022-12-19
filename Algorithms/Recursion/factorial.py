from time import perf_counter
Large_number = 900


def loop_fac(n):
    prod = 1
    for i in range(1, n):
        prod *= i
    return prod


def rec_fac(n):
    if n == 0:
        return 1
    else:
        return n*rec_fac(n-1)


def tail_fac(n):
    def go(n, ack):
        if n == 0:
            return ack
        else:
            return go(n-1, n*ack)
    return go(n, 1)


for i in range(10):
    print(loop_fac(i))
#     print(rec_fac(i))
    print(tail_fac(i))

t0 = perf_counter()
loop_fac(Large_number)
print(f"with loop: {perf_counter()-t0}")

t0 = perf_counter()
tail_fac(Large_number)
print(f"with tail recursion: {perf_counter()-t0}")


# t0 = perf_counter()
# rec_fac(Large_number)
# print(f"with recursion: {perf_counter()-t0}")
