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


x = [5, 3, 8, 1, 0]
print(x)
y = quick_sort(x)
print(y)
