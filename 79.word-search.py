#
# @lc app=leetcode.cn id=79 lang=python3
#
# [79] Word Search
#
# https://leetcode.cn/problems/word-search/description/
#
# algorithms
# Medium (46.49%)
# Likes:    1524
# Dislikes: 0
# Total Accepted:    399K
# Total Submissions: 858.4K
# Testcase Example:  '[["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]\n"ABCCED"'
#
# Given an m x n grid of characters board and a string word, return true if
# word exists in the grid.
# 
# The word can be constructed from letters of sequentially adjacent cells,
# where adjacent cells are horizontally or vertically neighboring. The same
# letter cell may not be used more than once.
# 
# 
# Example 1:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCCED"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "SEE"
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word
# = "ABCB"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
# 
# 
# 
# Follow up: Could you use search pruning to make your solution faster with a
# larger board?
# 
#

# @lc code=start
# Snowflake VOE
# TC: O(mn*4^k)  SC: O(mn)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, pos):
            nonlocal exist
            visited[i][j] = True
            if pos == len(word):
                exist = True
                return
            for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                newi = i+dx
                newj = j+dy
                if 0 <= newi < m and 0 <= newj < n and board[newi][newj] == word[pos] and not visited[newi][newj]:
                    dfs(newi, newj, pos+1)
                    if exist: return
                    # backtrack
                    visited[newi][newj] = False

        m, n = len(board), len(board[0])
        exist = False
        for i in range(m):
            for j in range(n):
                if word[0] == board[i][j]:
                    visited = [[False for _ in range(n)] for _ in range(m)]
                    dfs(i, j, 1)
                    if exist: return True
        return False
# @lc code=end

