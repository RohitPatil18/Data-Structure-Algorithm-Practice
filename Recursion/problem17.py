# The factorial of n 

def factorial(n):
  if n == 1:
    return 1
  return factorial(n-1) * n

if __name__ == '__main__':
  for i in range(0, 10):
    if i == 0:
      print(1)
    else:
      print(f'Factorial of {i} = {factorial(i)}')