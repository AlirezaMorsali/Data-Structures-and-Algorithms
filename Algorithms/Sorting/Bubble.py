
def bubble_sort(x: list):
    l = len(x)
    for i in range(l):
        for j in range(i, l):
            x[i], x[j] = (x[i], x[j]) if x[i] <= x[j] else (x[j], x[i])
    return x


x = ['a', 'x', 'h']
x = [5, 3, 8, 1, 0]
print(x)
y = bubble_sort(x)
print(y)
