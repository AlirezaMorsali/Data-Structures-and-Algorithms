"""
215. Kth Largest Element in an Array
Medium
12.8K
642
Companies

Given an integer array nums and an integer k, return the kth largest element in the array.

Note that it is the kth largest element in the sorted order, not the kth distinct element.

You must solve it in O(n) time complexity.
"""


def findkthlargest(x, k):
    position = len(x)-k

    def quick_sort_inplace(x: list, left, right):
        if left >= right:
            return
        else:
            j = left
            for i in range(left, right):
                if x[i] <= x[right]:
                    x[j], x[i] = x[i], x[j]
                    j += 1
                i += 1
            x[j], x[right] = x[right], x[j]
        if position == j:
            return x[j]
        elif position < j:
            return quick_sort_inplace(x, left, j-1)
        else:
            return quick_sort_inplace(x, j+1, right)

    return quick_sort_inplace(x, 0, len(x)-1)


y = [5, 1, 1, 2, 0, 0]
print(y)
print("QuickSelect")
print(findkthlargest(y, 2))
