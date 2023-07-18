# Number of Steps to Reduce a Number to Zero

def number_of_steps(n, cnt):
  if n == 0:
    return cnt
  if n % 2 == 0:
    n = n // 2
  else:
    n = n - 1
  return number_of_steps(n, cnt+1)

if __name__ == '__main__':
  for n in (14, 8, 89):
    print(f'Number of steps for {n}: {number_of_steps(n, 0)}')

