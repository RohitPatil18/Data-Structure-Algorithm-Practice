"""
You have n coins and you want to build a staircase with these coins. 
The staircase consists of k rows where the ith row has exactly i coins. 
The last row of the staircase may be incomplete.

Given the integer n, return the number of complete rows of the staircase you will build.
"""
####### NOT A BINARY SEARCH SOLUTION #######

def arrangeCoins(n: int) -> int:
    row = 1
    while n >= row:
        n = n - row
        row += 1
    return row - 1


def print_result(n: int) -> None:
    print(f'N: {n}, Rows: {arrangeCoins(n)}')

print_result(3)
print_result(15)
