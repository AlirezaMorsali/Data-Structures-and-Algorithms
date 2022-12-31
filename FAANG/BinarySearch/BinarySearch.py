"""
34. Find First and Last Position of Element in Sorted Array
Medium
15.2K
363
Companies

Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def find(nums, target, left, right):
    if len(nums) == 1:
        return left if nums[left] == target else -1

    if left > right:
        return -1
    else:
        mid = left + ((right - left)//2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            return find(nums, target, mid+1, right)
        else:
            return find(nums, target, left, mid-1)


def searchRange(nums: List[int], target: int) -> List[int]:
    mid = find(nums, target, 0, len(nums)-1)
    if mid == -1:
        return [-1, -1]
    start = end = mid
    for i in range(mid-1, -1, -1):
        if nums[i] == target:
            start = i
        else:
            break
    for i in range(mid+1, len(nums)):
        if nums[i] == target:
            end = i
        else:
            break
    return [start, end]


y = [1, 1, 2, 3, 8, 29]
y = [5, 7, 7, 8, 8, 10]
y = [1, 8]
target = 8
print(y)
print(f"Find {target} in array {y}")
print(find(y, 8, 0, len(y)-1))
print(searchRange(y, 8))
