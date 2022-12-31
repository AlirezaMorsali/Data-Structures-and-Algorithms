from typing import Optional


def quick_sort(x: list, pivot: Optional[int] = None):
    l = len(x)
    if pivot is None:
        pivot = l//2
    if l <= 0:
        return x
    else:
        left = [item for item in x if x[pivot] > item]
        middle = [item for item in x if x[pivot] == item]
        right = [item for item in x if x[pivot] < item]
        return quick_sort(left)+middle+quick_sort(right)


def quick_sort_inplace(x: list, left, right, pivot=-1):
    if left >= right:
        return
    else:
        if (not left <= pivot <= right):
            pivot = right
        if pivot != right:
            x[pivot], x[right] = x[right], x[pivot]
        j = left
        for i in range(left, right):
            if x[i] <= x[right]:
                x[j], x[i] = x[i], x[j]
                j += 1
            i += 1
        x[j], x[right] = x[right], x[j]

    quick_sort_inplace(x, left, j-1)
    quick_sort_inplace(x, j+1, right)
    return


def quick_sort_semi_inplace(x: list, pivot=-1):
    if (xlen := len(x)) <= 1:
        return x
    else:
        if pivot != -1:
            x[pivot], x[-1] = x[-1], x[pivot]
        i = j = 0
        while i < xlen-1:
            if x[i] <= x[-1]:
                x[j], x[i] = x[i], x[j]
                j += 1
            i += 1
        x[j], x[-1] = x[-1], x[j]

    x[:j] = quick_sort_semi_inplace(x[:j])
    x[j+1:] = quick_sort_semi_inplace(x[j+1:])
    return x


# x = [5, 3, 8, 1, 0]
# print(x)
# print("quick sort")
# y = quick_sort(x)
# print(y)

y = [3, 1, 5, 1]
y = [5, 1, 1, 2, 0, 0]
# x = [0, 1, 0]
print(y)
print("inplace quick sort")
quick_sort_inplace(y, 0, len(y)-1)
print(y)
