#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Medium (27.12%)
# Likes:    8483
# Dislikes: 10739
# Total Accepted:    2.3M
# Total Submissions: 8.4M
# Testcase Example:  '123'
#
# Given a signed 32-bit integer x, return x with its digits reversed. If
# reversing x causes the value to go outside the signed 32-bit integer range
# [-2^31, 2^31 - 1], then return 0.
#
# Assume the environment does not allow you to store 64-bit integers (signed or
# unsigned).
#
#
# Example 1:
#
#
# Input: x = 123
# Output: 321
#
#
# Example 2:
#
#
# Input: x = -123
# Output: -321
#
#
# Example 3:
#
#
# Input: x = 120
# Output: 21
#
#
#
# Constraints:
#
#
# -2^31 <= x <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        ans: int = -int(str(abs(x))[::-1]) if x < 0 else int(str(abs(x))[::-1])
        return 0 if ans < -2 ** 31 or ans > 2 ** 31 - 1 else ans


print(Solution.reverse(None, -321))
# @lc code=end
