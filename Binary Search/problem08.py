'''
Given a characters array letters that is sorted in non-decreasing order and 
a character target, return the smallest character in the array that is larger than target.

Note that the letters wrap around.

For example, if target == 'z' and letters == ['a', 'b'], the answer is 'a'.
 
Example 1:

Input: letters = ["c","f","j"], target = "a"
Output: "c"
'''
from typing import List

def nextGreatestLetter(letters: List[str], target: str) -> str:
    start = 0
    end = len(letters) - 1
    result = letters[start]
    while start <= end:
        mid = start + (end - start) // 2
        if letters[mid] > target:
            end = mid - 1
            result = letters[mid]
        else:
            start = mid + 1
    return result


def print_result(letters: List[str], target: str) -> None:
    print(f'Letters: {letters}, Target: {target}, '+ 
        f'Result: {nextGreatestLetter(letters, target)}')


print_result(["c","f","j"], "a")
print_result(["c","f","j"], "c")
print_result(["c","f","j"], "d")
print_result(["c","f","j"], "g")
print_result(["c","f","j"], "j")