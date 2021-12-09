"""
Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
find two numbers such that they add up to a specific target number. Let these two numbers be
numbers[index1] and numbers[index2] where 1 <= index1 < index2 <= numbers.length.

Return the indices of the two numbers, index1 and index2, added by one as an integer array 
[index1, index2] of length 2.

The tests are generated such that there is exactly one solution. You may not use the same element twice.
"""

from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]:
    start = 0
    end = len(numbers) - 1

    while start < end:
        result = numbers[start] + numbers[end]
        if target == result:
            return [start+1, end+1]
        elif result > target:
            end -= 1
        else:
            start += 1
    return [-1, -1]


def print_result(numbers: List[int], target: int) -> None:
    print(f'Numbers: {numbers}, Target: {target}, Indices: {twoSum(numbers, target)}')

print_result([2,7,11,15], 9)
print_result([2,3,4], 6)
print_result([-1,0], -1) 
print_result([3,24,50,79,88,150,345], 200)
