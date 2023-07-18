"""
Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, such as pow(x, 0.5) or x ** 0.5.
"""

# Binary Search Implementation
def findSqrt(x: int) -> int:
    start = 1
    end = x

    while start <= end:
        mid = start + (end - start) // 2
        res = mid * mid
        if res == x:
            return mid
        if res > x:
            end = mid - 1
        else:
            start = mid + 1
    return start - 1

print(findSqrt(63))
