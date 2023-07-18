"""
Given a positive integer num, write a function which returns True 
if num is a perfect square else False.
Follow up: Do not use any built-in library function such as sqrt.
"""

def isPerfectSquare(num: int) -> bool:
    start = 1 
    end = num
    while start <= end:
        mid = start  + (end - start) // 2
        sqr = mid * mid
        if sqr == num:
           return True
        if sqr <= num:
            start = mid + 1
        else:
            end = mid - 1
    return False

def print_result(num: int) -> None:
    print(f'{num}: {isPerfectSquare(num)}')

print_result(16)
print_result(10)
print_result(9)
print_result(19739)
print_result(197393767)