#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.cn/problems/nth-digit/description/
#
# algorithms
# Medium (45.66%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    55.1K
# Total Submissions: 120.6K
# Testcase Example:  '3'
#
# Given an integer n, return the n^th digit of the infinite integer sequence
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
#
#
# Example 1:
#
#
# Input: n = 3
# Output: 3
#
#
# Example 2:
#
#
# Input: n = 11
# Output: 0
# Explanation: The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, ... is a 0, which is part of the number 10.
#
#
#
# Constraints:
#
#
# 1 <= n <= 2^31 - 1
#
#
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        # TC: O(logn)  SC: O(1)
        lenn = 1
        while lenn*9*10**(lenn-1) < n:  # all numbers with lenn digits in total have lenn*9*10**(lenn-1) digits
            n -= lenn*9*10**(lenn-1)
            lenn += 1
        # now n has lenn digits
        start = 10**(lenn-1)
        end = start+(n-1)//lenn
        return int(str(end)[(n-1)%lenn])
# @lc code=end