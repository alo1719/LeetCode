from collections import *
from typing import *

class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            nonlocal dir
            for k, (di, dj) in enumerate([(1,0),(-1,0),(0,1),(0,-1)]):
                if 0 <= i+di < m and 0 <= j+dj < n and grid[i+di][j+dj]:
                    grid[i+di][j+dj] = 0
                    dir.append(k+1)
                    dfs(i+di, j+dj)
                    dir.append(-k-1)  # also need to record backtrack
        
        d = defaultdict(int)
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    dir = []
                    grid[i][j] = 0
                    dfs(i, j)
                    d[tuple(dir)] += 1
        return len(d)

print(Solution().numDistinctIslands([[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]))  # 1
print(Solution().numDistinctIslands([[1,1,0,1,1],[1,0,0,0,0],[0,0,0,0,1],[1,1,0,1,1]]))  # 3
print(Solution().numDistinctIslands([[1, 1], [1, 0], [0, 0], [1, 0], [1, 1]]))  # 2