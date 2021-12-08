

def fib(n):
  if n < 2:
    return 0, 1
  i, j = fib(n-1)
  return j, i+j



if __name__ == '__main__':
  n = 4
  if n == 0:
    ans =  0
  else:
    _, ans = fib(n)
  print(ans)