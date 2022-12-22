from typing import List
import math


def maxArea(height: List[int]) -> int:
    solution = 0
    ind = 1
    end = len(height)
    p1 = - math.inf
    p2 = - math.inf
    for i in range(end-1):
        if height[i] < p1:
            continue
        for j in range(ind, end):
            area = (j-i)*min(height[i], height[j])
            if area > solution:
                solution = area
                ind = j
                p1 = height[i]
                p2 = height[j]

    return solution


x = [2, 3, 4, 5, 18, 17, 6]
print(maxArea(x))
