# First uppercase letter in a string


def find_first_upper(text, i):
  if i == len(text): 
    return None
  elif text[i].isupper():
    return text[i]
  return find_first_upper(text, i+1)


if __name__ == '__main__':
  text = 'geeksForGeeks'
  c = find_first_upper(text, 0)
  if c:
    print(f'First upper case letter: {c}')
  else:
    print('No upper case letter in given string.')
  