# Write a function that reverses a string. The input string is given as an array of characters s.

def reverse_string(text, i, n):
  if i == n:
    return text[i]
  return reverse_string(text, i+1, n) + text[i]
  

if __name__ == '__main__':
  text = 'reverse_string_example'
  n = len(text) - 1 
  print(reverse_string(text, 0, n))

