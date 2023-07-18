# Recursive Programs to find Minimum and Maximum elements of array

def getMinMax(nums):
  if len(nums) == 1:
    return nums[0], nums[0]
  min, max = getMinMax(nums[1:])
  if min > nums[0]:
    min = nums[0]
  elif max < nums[0]:
    max = nums[0]
  return min, max

if __name__ == '__main__':
  nums = [1, 2, 4, 6, -8, 89]
  min, max = getMinMax(nums)
  print(f'min = {min}, max = {max}')