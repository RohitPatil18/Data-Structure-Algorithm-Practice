# Recursive Insertion Sort

def sort(nums, i, j, n):
  if i == n:
    return nums
  elif j == 0 or nums[j-1] < nums[j]:
    return sort(nums, i+1, i+1, n)
  nums[j-1], nums[j] = nums[j], nums[j-1]
  return sort(nums, i, j-1, n)
  


if __name__ == '__main__':
  nums = [7, 4, 3, -4, 5, 8, -19]
  print(sort(nums, 1, 1, len(nums)))