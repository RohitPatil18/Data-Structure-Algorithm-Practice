# Sum of natural numbers using recursion

def sum(left, right):
  if left == right:
    return left
  elif left > right:
    return 0
  return left + right + sum(left+1, right-1)

if __name__ == '__main__':
  n = 5
  print(sum(1, n))