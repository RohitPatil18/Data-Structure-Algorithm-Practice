# Program for length of a string using recursion

def length(text):
  if text == '':
    return 0
  return 1 + length(text[1:])

if __name__ == '__main__':
  text ="hellothere"
  print(length(text))