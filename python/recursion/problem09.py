# Sum of digit of a number using recursion

def sum_of_digits(num):
  if num // 10 == 0:
    return num
  return sum_of_digits(num//10) + num % 10


if __name__ == '__main__':
  num = 45632
  print(sum_of_digits(num))