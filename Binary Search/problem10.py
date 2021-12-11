'''
Given a sorted numsay of distinct integers and a target value, 
return the index if the target is found. If not, return the index 
where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
'''
from typing import List

def searchInsert(nums: List[int], target: int) -> int:
    start = 0
    end = len(nums) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = start + 1
    return start


def print_result(nums: List[int], target: int) -> None:
    print(f'nums: {nums}, target: {target}, '+ 
        f'Result: {searchInsert(nums, target)}')


print_result([1,3,5,6], 5)
print_result([1,2,5,6], 4)
print_result([1,2,5,6], 7)
print_result([1], 0)


