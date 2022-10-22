# To retrive number of possible paths to reach from first 
# node to the very last node
#
# Example:
# 1 1 1 1
# 1 1 1 1
# 1 1 1 1
#
# result = 10
#
# 1 1 0 1
# 1 1 1 1
# 1 1 0 1
#
# result = 2


rows = 3
cols = 4
matrix = [[1, 1, 0, 1],[1, 1, 1, 1],[1,  1, 0, 1]]

known_paths = {}

def numPaths(row, col):
    # To cheack if node is already visited and no of possible 
    # paths are known
    key = f"path-{row}-{col}"
    paths = known_paths.get(key)
    if paths:
        return paths
    
    
    if matrix[row][col] == 0:
        paths = 0  
    elif row == rows-1 and col == cols-1:
        paths = 1
    elif row == rows-1:
        paths = numPaths(row, col+1)
    elif col == cols-1:
        paths = numPaths(row+1, col)
    else:
        paths = numPaths(row+1, col) + numPaths(row, col+1)
    
    # Stores value to avoid recursing  same node again and again
    known_paths[key] = paths
    return paths
    
print(numPaths(0, 0))
