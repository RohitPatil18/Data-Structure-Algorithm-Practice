'''
Let's call an array arr a mountain if the following properties hold:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... arr[i-1] < arr[i]
arr[i] > arr[i+1] > ... > arr[arr.length - 1]
Given an integer array arr that is guaranteed to be a mountain, 
return any i such that arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1].
'''

from typing import List

def peakIndexInMountainArray(arr: List[int]) -> int:
    start = 0
    end = len(arr) - 1
    
    while start < end:
        mid = start + (end - start) // 2
        if arr[mid] < arr[mid+1]:
            start = mid + 1
        else:
            end = mid
    return start


def print_result(arr: List[int]) -> None:
    print(f'arr: {arr}, '+ 
        f'Result: {peakIndexInMountainArray(arr)}')


print_result([0,1,0])
print_result([0,2,1,0])
print_result([102,69,100,101,79,78,67,36,26,19])



