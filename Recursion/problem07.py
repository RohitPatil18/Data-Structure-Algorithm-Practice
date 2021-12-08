# Recursive Bubble Sort

def sort(nums, i, j, n):
  if i == n:
    return nums
  elif j > n:
    return sort(nums, i+1, i+2, n)
  if nums[i] > nums[j]:
    nums[i], nums[j] = nums[j], nums[i] 
  return sort(nums, i, j+1, n)


if __name__ == '__main__':
  nums = [7,4, 3, -4, 5, 8]
  print(sort(nums, 0, 1, len(nums)-1))