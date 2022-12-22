from typing import List


def trap(height: List[int]) -> int:
    p1 = 0
    p2 = 0
    s = 0
    t = 0
    next_max = 0
    while p2 < len(height)-1:
        if p1 == p2:
            # print("p1==p2")
            # print(f"p1:{p1}, p2:{p2}")
            if height[p1+1] >= height[p1]:
                p1 += 1
                p2 += 1
            else:
                p2 += 1
        else:
            if height[p2 + 1] >= height[p1]:
                # full bucket
                p2 += 1
                # print(f"p1:{p1}, p2:{p2}")
                edge = min(height[p2], height[p1])
                for i in range(p1+1, p2):
                    s += (edge-height[i])
                p1 = p2
                next_max = p2 + 1
                # print(f"p1:{p1}, p2:{p2}")
            else:
                p2 += 1
                if height[p2] >= height[next_max]:
                    next_max = p2
                # Continue bucket
    edge = min(height[next_max], height[p1])
    for i in range(p1+1, next_max):
        s += (edge-height[i])

    return s


x = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(trap(x))
