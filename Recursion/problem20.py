# Given two positive integers n and k, the binary string  Sn is formed as follows:

# S1 = "0"
# Si = Si-1 + "1" + reverse(invert(Si-1)) for i > 1
# Where + denotes the concatenation operation, reverse(x) returns the reversed string x, 
# and invert(x) inverts all the bits in x (0 changes to 1 and 1 changes to 0).

# For example, the first 4 strings in the above sequence are:

# S1 = "0"
# S2 = "011"
# S3 = "0111001"
# S4 = "011100110110001"
# Return the kth bit in Sn. It is guaranteed that k is valid for the given n.

def inverse(ch):
  if ch == '1':
    return '0'
  return '1'

def reverse(chars):
  res = ''
  for ch in chars[::-1]:
    res = res + inverse(ch)
  return res

def series(n):
  if n == 1:
    return '0'
  s_prev = series(n-1)
  s = s_prev + '1' + reverse(s_prev)
  return s

def kth_bit(n, k):
  s = series(n)
  return s[k-1]

if __name__ == '__main__':
  n = 20
  k = 100000
  print(kth_bit(n, k))



# import enum
# class UserType(enum.Enum):
#   ADMIN = 1
#   USER = 2
# print(UserType.ADMIN.value)
# print('Admin' == UserType.ADMIN)
# Checking
# if user.user_type == 'Amdin':
#   return True
