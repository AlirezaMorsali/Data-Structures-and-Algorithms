def insertion_sort(x: list):
    l = len(x)
    for i in range(l):
        ind = 0
        for j in reversed(range(i)):
            print(f"i:{i}, j:{j}")
            if x[i] < x[j]:
                continue
            else:
                ind = j
                break
        x.insert(ind, x.pop(i))
    return x


# x = ['a', 'x', 'h']
x = [5, 3, 8, 1, 0]
print(x)
y = insertion_sort(x)
print(y)
