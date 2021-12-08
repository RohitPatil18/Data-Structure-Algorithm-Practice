# Program to check if an array is sorted or not

def is_array_sorted(nums, i, size):
  if i == size:
    return 'Yes'
  if nums[i-1] > nums[i]:
    return 'No'
  return is_array_sorted(nums, i+1, size)

if __name__ == '__main__':
  a = (2, 3, 5, 8)
  b = (2, 3, 9, 1)
  for i in (a, b):
    size = len(i)
    print(f'Is {i} sorted? Ans: {is_array_sorted(i, 1, size)}')