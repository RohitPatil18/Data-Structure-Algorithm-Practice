# A digit string is good if the digits (0-indexed) at even indices are even and the digits at odd indices are prime (2, 3, 5, or 7).

# For example, "2582" is good because the digits (2 and 8) at even positions are even and the digits (5 and 2) at odd positions are prime. However, "3245" is not good because 3 is at an even index but is not even.
# Given an integer n, return the total number of good digit strings of length n. Since the answer may be large, return it modulo 109 + 7.

# A digit string is a string consisting of digits 0 through 9 that may contain leading zeros.

def calc(num, power):
  # print(f'Num: {num}, power: {power}')
  if power == 1:
    return num
  rem = power % 2
  power = power // 2
  return ((calc(num, power) ** 2) * (num ** rem)) % 1000000007

if __name__ == '__main__':
  n = 50
  j = n // 2 
  i = n - j
  left = calc(5, i) if i > 0 else 1
  right = calc(4, j) if j > 0 else 1
  print(left * right % 1000000007)