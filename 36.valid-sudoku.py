#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#
# https://leetcode.com/problems/valid-sudoku/description/
#
# algorithms
# Medium (56.56%)
# Likes:    6457
# Dislikes: 796
# Total Accepted:    875.8K
# Total Submissions: 1.5M
# Testcase Example:  '[["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]'
#
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be
# validated according to the following rules:
#
#
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9
# without repetition.
#
#
# Note:
#
#
# A Sudoku board (partially filled) could be valid but is not necessarily
# solvable.
# Only the filled cells need to be validated according to the mentioned
# rules.
#
#
#
# Example 1:
#
#
# Input: board =
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
#
# Example 2:
#
#
# Input: board =
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner
# being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it
# is invalid.
#
#
#
# Constraints:
#
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.
#
#
#

# @lc code=start
from typing import List


class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] != ".":
                    if board[i][j] in board[i][j + 1:]:
                        print("1 ", i, " ", j, " ", board[i][j])
                        return False
                    temp = board[i][j]
                    board[i][j] = "."
                    if temp in [board[k][j] for k in range(len(board))]:
                        print("2 ", i, " ", j, " ", board[i][j])
                        print([board[k][j] for k in range(len(board))])
                        return False
                    if temp in [
                            board[3 * (i // 3) + k][3 * (j // 3) + l]
                            for k in range(3) for l in range(3)
                    ]:
                        print("3 ", i, " ", j, " ", board[i][j])
                        return False
                    board[i][j] = temp
        return True


print(Solution().isValidSudoku([["5", "3", ".", ".", "7", ".", ".", ".", "."],
                                ["6", ".", ".", "1", "9", "5", ".", ".", "."],
                                [".", "9", "8", ".", ".", ".", ".", "6", "."],
                                ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
                                ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
                                ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
                                [".", "6", ".", ".", ".", ".", "2", "8", "."],
                                [".", ".", ".", "4", "1", "9", ".", ".", "5"],
                                [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))

# @lc code=end
