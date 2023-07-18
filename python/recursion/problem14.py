# Given an integer n, return true if it is a power of three. Otherwise, return false.

def check(n):
  res = n // 3
  rem = n % 3
  if rem != 0 or res < 3:
    return False
  elif res == 3:
    return True
  return check(res)

if __name__ == '__main__':
  for n in (9, 27, 1, 0, 16, 32, 64, 63563, 5267):
    if n == 1 or n == 3:
      print(True)
    else:
      print(check(n))
