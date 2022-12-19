import heapq


def heap_sort(x: list):
    heapq.heapify(x)
    return [heapq.heappop(x) for _ in range(len(x))]


x = [10, 11, 8, 9, 2, 3, 7]

print(x)
y = heap_sort(x)
print(y)
print(x)
