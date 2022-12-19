
def merge_sort(x: list):
    if (l := len(x)) == 1:
        return x
    else:
        return merge(merge_sort(x[:l//2]), merge_sort(x[l//2:]))
    pass


def merge(x: list, y: list):
    if (lx := len(x)) == 0:
        return y
    elif (ly := len(y)) == 0:
        return x
    else:
        if x[0] < y[0]:
            return [x[0]] + merge(x[1:], y)
        else:
            return [y[0]] + merge(x, y[1:])


x = [5, 3, 8, 1, 0]
x = [11, 31, 7, 41, 101, 56, 77, 2]
print(x)
y = merge_sort(x)
print(y)
