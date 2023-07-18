# Recursive program for prime number

def is_prime(n, i):
  if i * i > n:
    return True
  elif n % i == 0:
    return False
  return is_prime(n, i+1)

if __name__ == '__main__':
  n = 17
  if n < 2:
    print("Number should be greater than 1.")
  print(is_prime(n, 2))