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
# TC: O(logn)  SC: O(1)
class Solution:
    def reverse(self, x: int) -> int:
        if not x: return 0
        neg = x < 0
        while x%10 == 0: x //= 10
        x = str(abs(x))[::-1]
        if neg:
            if '0'*(len(str(2**31))-len(x))+x > str(2**31): return 0
            return -int(x)
        else:
            if '0'*(len(str(2**31-1))-len(x))+x > str(2**31-1): return 0
            return int(x)


print(Solution.reverse(None, -321))
# @lc code=end
