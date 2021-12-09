"""
Given an array of integers nums sorted in non-decreasing order, 
find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List

def searchRange(nums: List[int], target: int) -> List[int]:
    start, end = 0, len(nums)-1

    while start <= end and nums[start] <= target and  nums[end] >= target:
        if nums[start] == target and nums[end] == target:
            return [start, end]
        elif nums[start] == target:
            end -= 1
        elif nums[end] == target:
            start += 1
        else:
            start, end = start+1, end-1
    return [-1, -1]


def print_result(numbers: List[int], target: int) -> None:
    print(f'Numbers: {numbers}, Target: {target}, Indices: {searchRange(numbers, target)}')

print_result([5,7,7,8,8,10], 8)
print_result([5,7,7,8,8,10], 6)
print_result([], 0) 
