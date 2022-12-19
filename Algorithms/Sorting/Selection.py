def selection_sort(x: list):
    l = len(x)
    for i in range(l):
        ind = i
        for j in range(i+1, l):
            if x[ind] > x[j]:
                ind = j
        x[i], x[ind] = x[ind], x[i]
    return x


x = ['a', 'x', 'h']
x = [5, 3, 8, 1, 0]
print(x)
y = selection_sort(x)
print(y)
