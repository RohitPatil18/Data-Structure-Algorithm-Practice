# We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, 
# we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

# For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
# Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

import math

def get_position(n: int, k: int, inv: int):
  if n == 2:
    return k, inv
  size = math.pow(2, n-1) // 2
  # print(f"n: {n}, k: {k}, size: {size}, inv: {inv}")
  if size >= k:
    return get_position(n-1, k, inv)  
  return get_position(n-1, k-size, inv+1)  
  
def invert_bit(bit: int) -> int:
  return 0 if bit == 1 else 1

if __name__ == '__main__':
  n = 6
  ks  = (1, 2, 3, 4, 32, 31, 30)
  for _k in ks:
    k, inv = get_position(n, _k, inv=0)
    # print(k, " ", inv)
    bit = 0 if k == 1 else 1
    for i in range(0, inv):
      bit = invert_bit(bit)
    print(bit)