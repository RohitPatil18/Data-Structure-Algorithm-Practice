# Given an array of integers, print a sum triangle from it such that the first level has all array elements. 
# From then, at each level number of elements is one less than the previous level and elements at the level is
# be the Sum of consecutive two elements in the previous level. 

def buildRow(nums, triangle):
  row = []
  for i in range(len(nums) - 1):
    row.append(nums[i]+nums[i+1])
  triangle.append(row)
  if len(nums) != 2:
    triangle = buildRow(row, triangle)
  return triangle

def mySolution(nums):
  '''
  Solution I came up with on my very first try. There are a lot of unnecessary things are done here.
  - Passing triangle array will increase memory usage
  - Another loop for printing rows 

  Time ComplexityK O(2n). n is number of rows
  '''
  triangle = [nums]
  triangle = buildRow(nums, triangle)
  for i in range(len(triangle), 0, -1):
    print(triangle[i-1])

###############################################################3

def printTriangle(nums):
  nextRow = []
  if len(nums) == 1:
    print(nums)
    return
  for i in range(0, len(nums)-1):
    nextRow.append(nums[i] + nums[i+1])
  printTriangle(nextRow)
  print(nums)

def optimizedSolution(nums):
  '''
  Optimized solution I referred once I finished my solution.
  Time complexity: O(n) --> n! 
  // actually if n = number of elements
  '''
  printTriangle(nums)

if __name__ == '__main__':
  nums = [1, 2, 3, 4, 5]
  mySolution(nums)
  print('-------------------')
  optimizedSolution(nums)