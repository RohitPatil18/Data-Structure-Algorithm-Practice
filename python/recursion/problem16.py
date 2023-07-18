# Write a recursive function for given n and a to determine x:
#       n = a ^ x 
#       a = 2, 3, 4
#       (2 ^ -31) <= n <= (2 ^ 31) - 1    

def findX(n, a, x, ans):
  if ans == n:
    return x
  elif ans > n:
    return None
  return findX(n, a, x+1, ans*a)

if __name__ == '__main__':
  for n, a in ((9, 3), (64, 2), (16, 4)):
    print(f'n: {n}, a: {a}, ans: {findX(n, a, 1, a)}')
