from time import perf_counter

Large_number = 100


def loop_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        nm1 = 1
        nm2 = 0
        for _ in range(n-1):
            temp = nm2 + nm1
            nm2 = nm1
            nm1 = temp
        return nm1


def rec_fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return rec_fib(n-1) + rec_fib(n-2)


def tail_fib(n):
    def helper(n, nm1, nm2):
        if n == 0:
            return nm1
        elif n == 1:
            return nm2
        else:
            return helper(n-1, nm1+nm2, nm1)

    return helper(n, 0, 1)


for i in range(10):
    print(loop_fib(i))
    # print(rec_fib(i))
    print(tail_fib(i))

t0 = perf_counter()
print(loop_fib(Large_number))
print(f"with loop: {perf_counter()-t0}")

t0 = perf_counter()
print(tail_fib(Large_number))
print(f"with tail recursion: {perf_counter()-t0}")


# t0 = perf_counter()
# print(rec_fib(Large_number))
# print(f"with recursion: {perf_counter()-t0}")
