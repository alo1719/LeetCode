# TC: O(n^2)
# SC: O(n)
def validateSudoku(grid):
    n = len(grid)
    for i in range(n):
        tmp = [False] * n
        for j in range(n):
            if grid[i][j] < 1 or grid[i][j] > n or tmp[grid[i][j]-1]:
                return False
            tmp[grid[i][j]-1] = True
    for j in range(n):
        tmp = [False]*n
        for i in range(n):
            if grid[i][j] < 1 or grid[i][j] > n or tmp[grid[i][j]-1]:
                return False
            tmp[grid[i][j]-1] = True
    return True

print(validateSudoku([[1,2,3],[2,3,1],[3,1,2]]))  # True