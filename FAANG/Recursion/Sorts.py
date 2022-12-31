

def merge_sort(lst):
    if (length := len(lst)) <= 1:
        return lst
    else:
        return merge(merge_sort(lst[:length//2]), merge_sort(lst[length//2:]))


def merge(lst1, lst2):
    if len(lst1) == 0:
        return lst2
    elif len(lst2) == 0:
        return lst1
    else:
        if (l1 := lst1[0]) <= (l2 := lst2[0]):
            return [l1] + merge(lst1[1:], lst2)
        else:
            return [l2] + merge(lst1, lst2[1:])


def quick_sort(lst, pvt=None):
    if pvt is None:
        pvt = len(lst)//2
    if len(lst) <= 1:
        return lst
    else:
        right = quick_sort(list(filter(lambda x: x < lst[pvt], lst)))
        middle = list(filter(lambda x: x == lst[pvt], lst))
        left = quick_sort(list(filter(lambda x: x > lst[pvt], lst)))
        return right + middle + left


x = [5, 3, 2, 7, 1]
print(x)
print("merge sort:")
print(merge_sort(x))

print("Quick sort:")
print(quick_sort(x))
