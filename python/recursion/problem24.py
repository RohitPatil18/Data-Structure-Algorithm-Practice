mod = 10 ** 9 + 7

def calculate(num, power):
  if power == 1:
    return num
  res = calculate(num, power//2)
  if power % 2 == 0:
    return res * res % mod
  return res * res * num % mod

p = 22
length = 2 ** p - 1
print(calculate(length-1, length // 2) * length % mod)