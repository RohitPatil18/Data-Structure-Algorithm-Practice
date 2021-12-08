# Given an integer n, return true if it is a power of two. Otherwise, return false.

def check(n):
  res = n // 2
  rem = n % 2
  if rem != 0 or res < 2:
    return False
  elif res == 2:
    return True
  return check(res)

if __name__ == '__main__':
  for n in (2, 4, 8, 16, 32, 64, 63563, 5267):
    if n == 1 or n == 2:
      print(True)
    else:
      print(check(n))
