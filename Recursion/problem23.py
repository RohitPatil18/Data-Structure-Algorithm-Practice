

def calculate(num, power):
  if power == 1:
    return num
  res = calculate(num, power//2)
  if power % 2 == 0:
    return res * res
  return res * res * num

if __name__ == "__main__":
  num = 2
  power = -3
  if power > 0:
    print(calculate(num, power))
  else:
    print(1 / calculate(num, 0 - power))