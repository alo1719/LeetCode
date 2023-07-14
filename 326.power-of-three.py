#
# @lc app=leetcode id=326 lang=python3
#
# [326] Power of Three
#
# https://leetcode.com/problems/power-of-three/description/
#
# algorithms
# Easy (45.13%)
# Likes:    2087
# Dislikes: 198
# Total Accepted:    594.2K
# Total Submissions: 1.3M
# Testcase Example:  '27'
#
# Given an integer n, return true if it is a power of three. Otherwise, return
# false.
#
# An integer n is a power of three, if there exists an integer x such that n ==
# 3^x.
#
#
# Example 1:
#
#
# Input: n = 27
# Output: true
# Explanation: 27 = 3^3
#
#
# Example 2:
#
#
# Input: n = 0
# Output: false
# Explanation: There is no x where 3^x = 0.
#
#
# Example 3:
#
#
# Input: n = -1
# Output: false
# Explanation: There is no x where 3^x = (-1).
#
#
#
# Constraints:
#
#
# -2^31 <= n <= 2^31 - 1
#
#
#
# Follow up: Could you solve it without loops/recursion?
#

# @lc code=start
# TC: O(1)  SC: O(1)
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # pow = 1
        # while pow < 2**31:
        #     pow *= 3
        # print(pow)
        # 3486784401 / 3 = 1162261467
        return n > 0 and 1162261467 % n == 0


print(Solution().isPowerOfThree(1))

# @lc code=end
