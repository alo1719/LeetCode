#
# @lc app=leetcode id=864 lang=python3
#
# [864] Shortest Path to Get All Keys
#
# https://leetcode.com/problems/shortest-path-to-get-all-keys/description/
#
# algorithms
# Hard (45.58%)
# Likes:    1028
# Dislikes: 48
# Total Accepted:    32.2K
# Total Submissions: 70.4K
# Testcase Example:  '["@.a..","###.#","b.A.B"]'
#
# You are given an m x n grid grid where:
# 
# 
# '.' is an empty cell.
# '#' is a wall.
# '@' is the starting point.
# Lowercase letters represent keys.
# Uppercase letters represent locks.
# 
# 
# You start at the starting point and one move consists of walking one space in
# one of the four cardinal directions. You cannot walk outside the grid, or
# walk into a wall.
# 
# If you walk over a key, you can pick it up and you cannot walk over a lock
# unless you have its corresponding key.
# 
# For some 1 <= k <= 6, there is exactly one lowercase and one uppercase letter
# of the first k letters of the English alphabet in the grid. This means that
# there is exactly one key for each lock, and one lock for each key; and also
# that the letters used to represent the keys and locks were chosen in the same
# order as the English alphabet.
# 
# Return the lowest number of moves to acquire all keys. If it is impossible,
# return -1.
# 
# 
# Example 1:
# 
# 
# Input: grid = ["@.a..","###.#","b.A.B"]
# Output: 8
# Explanation: Note that the goal is to obtain all the keys not to open all the
# locks.
# 
# 
# Example 2:
# 
# 
# Input: grid = ["@..aA","..B#.","....b"]
# Output: 6
# 
# 
# Example 3:
# 
# 
# Input: grid = ["@Aa"]
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 30
# grid[i][j] is either an English letter, '.', '#', or '@'.
# The number of keys in the grid is in the range [1, 6].
# Each key in the grid is unique.
# Each key in the grid has a matching lock.
# 
# 
#

# @lc code=start
from functools import *

class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        m, n = len(grid), len(grid[0])
        startx = starty = k = 0
        d = {}
        for i in range(m):
           for j in range(n):
                if grid[i][j] == '@': startx, starty = i, j
                if grid[i][j] in 'abcdef':
                    d[grid[i][j]] = k
                    k += 1
        mask = (1<<k)-1  # 1->needs to obtain
        ans = 0
        dq = deque([(startx, starty, mask)])
        sett = set()
        while dq:
            lenn = len(dq)
            for _ in range(lenn):
                x, y, mask = dq.popleft()
                if mask == 0: return ans
                for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                    nx, ny = x+dx, y+dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != '#' and (nx, ny, mask) not in sett:  # in each state, we only need to visit each cell once
                        if grid[nx][ny] in 'abcdef' and (mask>>d[grid[nx][ny]])&1 == 1:
                            dq.append((nx, ny, mask^(1<<d[grid[nx][ny]])))
                            sett.add((nx, ny, mask))
                        elif grid[nx][ny] in 'ABCDEF' and (mask>>d[grid[nx][ny].lower()])&1 == 1:
                            continue
                        else:
                            dq.append((nx, ny, mask))
                            sett.add((nx, ny, mask))
            ans += 1
        return -1
# @lc code=end

