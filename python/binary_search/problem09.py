'''
Given an array arr of positive integers sorted in a strictly increasing 
order, and an integer k.
Find the kth positive integer that is missing from this array.

Example 1:

Input: arr = [2,3,4,7,11], k = 5
Output: 9
Explanation: The missing positive integers are [1,5,6,8,9,10,12,13,...]. 
The 5th missing positive integer is 9.
'''

### NOT A BINARY SEARCH - WORST TIME COMPLEXITY = O(n) ###

from typing import List

def findKthPositive(arr: List[int], k: int) -> int:
    seq = 1
    for n in arr:
        if n != seq:
            diff = n - seq
            if diff >= k:
                break
            k -= diff
        seq = n + 1
    return seq + k - 1

def findKthPositiveBinary(arr: List[int], k: int) -> int:
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = start + (end - start) // 2
        if arr[mid] - mid <= k:
            start = mid + 1
        else:
            end = mid - 1
    if arr[mid] - mid > k:
        return mid+k
    return mid+k+1


def print_result(arr: List[int], k: int) -> None:
    print(f'arr: {arr}, k: {k}, '+ 
        f'Result: {findKthPositiveBinary(arr, k)}')


print_result([2,3,7,7,11], 5)
print_result([1,2,3,4], 2)

