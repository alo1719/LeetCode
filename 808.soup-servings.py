#
# @lc app=leetcode.cn id=808 lang=python3
#
# [808] Soup Servings
#
# https://leetcode.cn/problems/soup-servings/description/
#
# algorithms
# Medium (58.76%)
# Likes:    228
# Dislikes: 0
# Total Accepted:    22.4K
# Total Submissions: 38.2K
# Testcase Example:  '50'
#
# There are two types of soup: type A and type B. Initially, we have n ml of
# each type of soup. There are four kinds of operations:
# 
# 
# Serve 100 ml of soup A and 0 ml of soup B,
# Serve 75 ml of soup A and 25 ml of soup B,
# Serve 50 ml of soup A and 50 ml of soup B, and
# Serve 25 ml of soup A and 75 ml of soup B.
# 
# 
# When we serve some soup, we give it to someone, and we no longer have it.
# Each turn, we will choose from the four operations with an equal probability
# 0.25. If the remaining volume of soup is not enough to complete the
# operation, we will serve as much as possible. We stop once we no longer have
# some quantity of both types of soup.
# 
# Note that we do not have an operation where all 100 ml's of soup B are used
# first.
# 
# Return the probability that soup A will be empty first, plus half the
# probability that A and B become empty at the same time. Answers within 10^-5
# of the actual answer will be accepted.
# 
# 
# Example 1:
# 
# 
# Input: n = 50
# Output: 0.62500
# Explanation: If we choose the first two operations, A will become empty
# first.
# For the third operation, A and B will become empty at the same time.
# For the fourth operation, B will become empty first.
# So the total probability of A becoming empty first plus half the probability
# that A and B become empty at the same time, is 0.25 * (1 + 1 + 0.5 + 0) =
# 0.625.
# 
# 
# Example 2:
# 
# 
# Input: n = 100
# Output: 0.71875
# 
# 
# 
# Constraints:
# 
# 
# 0 <= n <= 10^9
# 
# 
#

# @lc code=start
@cache
def f(i, j):
    if i <= 0 and j <= 0: return 0.5
    if i <= 0: return 1
    if j <= 0: return 0
    return (1/4)*(f(i-4, j)+f(i-3, j-1)+f(i-2, j-2)+f(i-1, j-3))

# TC: O(C^2)  SC: O(C^2)  C is the constant to output 1 directly
class Solution:
    def soupServings(self, n: int) -> float:
        # f[i][j] = (1/4)*(f[i-4][j]+f[i-3][j-1]+f[i-2][j-2]+f[i-1][j-3])
        n = ceil(n/25)
        return f(n, n) if n < 5000 else 1
# @lc code=end

