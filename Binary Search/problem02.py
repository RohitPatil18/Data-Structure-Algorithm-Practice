"""
We are playing the Guess Game. The game is as follows:

I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I will tell you whether the number I picked is higher or lower than your guess.

You call a pre-defined API int guess(int num), which returns 3 possible results:

-1: The number I picked is lower than your guess (i.e. pick < num).
1: The number I picked is higher than your guess (i.e. pick > num).
0: The number I picked is equal to your guess (i.e. pick == num).
Return the number that I picked.
"""

pick = 54

def guess(num: int) -> int:
    if num == pick:
        return 0
    elif pick < num:
        return -1
    return 1

def guessNumber(n:int) -> int:
    start = 0
    end = n
    while start <= end:
        mid = start + (end - start) // 2
        res = guess(mid)
        if res == 0:
            return mid
        elif res == -1:
            end = mid - 1
        else:
            start = mid + 1
    return start


print(guessNumber(100))