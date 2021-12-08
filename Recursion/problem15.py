# Given an integer n, return true if it is a power of four. Otherwise, return false.

def check(n):
  res = n // 4
  rem = n % 4
  if rem != 0 or res < 4:
    return False
  elif res == 4:
    return True
  return check(res)

if __name__ == '__main__':
  for n in (1, 0, 16, 32, 64, 63563, 5267):
    if n == 1 or n == 4:
      print(True)
    else:
      print(check(n))
