#
# @lc app=leetcode id=688 lang=python3
#
# [688] Knight Probability in Chessboard
#
# https://leetcode.com/problems/knight-probability-in-chessboard/description/
#
# algorithms
# Medium (56.32%)
# Likes:    3526
# Dislikes: 438
# Total Accepted:    139.5K
# Total Submissions: 247.7K
# Testcase Example:  '3\n2\n0\n0'
#
# On an n x n chessboard, a knight starts at the cell (row, column) and
# attempts to make exactly k moves. The rows and columns are 0-indexed, so the
# top-left cell is (0, 0), and the bottom-right cell is (n - 1, n - 1).
# 
# A chess knight has eight possible moves it can make, as illustrated below.
# Each move is two cells in a cardinal direction, then one cell in an
# orthogonal direction.
# 
# Each time the knight is to move, it chooses one of eight possible moves
# uniformly at random (even if the piece would go off the chessboard) and moves
# there.
# 
# The knight continues moving until it has made exactly k moves or has moved
# off the chessboard.
# 
# Return the probability that the knight remains on the board after it has
# stopped moving.
# 
# 
# Example 1:
# 
# 
# Input: n = 3, k = 2, row = 0, column = 0
# Output: 0.06250
# Explanation: There are two moves (to (1,2), (2,1)) that will keep the knight
# on the board.
# From each of those positions, there are also two moves that will keep the
# knight on the board.
# The total probability the knight stays on the board is 0.0625.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, k = 0, row = 0, column = 0
# Output: 1.00000
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 25
# 0 <= k <= 100
# 0 <= row, column <= n - 1
# 
# 
#

# @lc code=start
# TC: O(n^2*k)  SC: O(n^2)
class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # f[i][j] = sum(f_old[i-dx][j-dy])
        f = [[0]*n for _ in range(n)]
        f[row][column] = 1
        for _ in range(k):
            f_old = deepcopy(f)  # 2d, need deepcopy
            for i in range(n):
                for j in range(n):
                    f[i][j] = 0
                    for dx, dy in [(1,2), (1,-2), (-1,2), (-1,-2), (2,1), (2,-1), (-2,1), (-2,-1)]:
                        if 0 <= i+dx < n and 0 <= j+dy < n:
                            f[i][j] += f_old[i+dx][j+dy]
        return sum(map(sum, f))/8**k
# @lc code=end

