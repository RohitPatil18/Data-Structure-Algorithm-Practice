# Product of 2 Numbers using Recursion

def product(num1, num2):
  if num2 == 1:
    return num1
  return num1 + product(num1, num2-1)

if __name__ == "__main__":
  num1 = 6723
  num2 = 10
  if num1 < num2:
    print(product(num2, num1))
  else:
    print(product(num1, num2))