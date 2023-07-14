#
# @lc app=leetcode.cn id=202 lang=python3
#
# [202] Happy Number
#
# https://leetcode.cn/problems/happy-number/description/
#
# algorithms
# Easy (63.27%)
# Likes:    1197
# Dislikes: 0
# Total Accepted:    341.4K
# Total Submissions: 539.6K
# Testcase Example:  '19'
#
# Write an algorithm to determine if a number n is happy.
# 
# A happy number is a number defined by the following process:
# 
# 
# Starting with any positive integer, replace the number by the sum of the
# squares of its digits.
# Repeat the process until the number equals 1 (where it will stay), or it
# loops endlessly in a cycle which does not include 1.
# Those numbers for which this process ends in 1 are happy.
# 
# 
# Return true if n is a happy number, and false if not.
# 
# 
# Example 1:
# 
# 
# Input: n = 19
# Output: true
# Explanation:
# 1^2 + 9^2 = 82
# 8^2 + 2^2 = 68
# 6^2 + 8^2 = 100
# 1^2 + 0^2 + 0^2 = 1
# 
# 
# Example 2:
# 
# 
# Input: n = 2
# Output: false
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
# TC: O(logn)  SC: O(1)
class Solution:
    def isHappy(self, n: int) -> bool:
        def calc_next(n):
            ans = 0
            while n > 0:
                ans += (n%10)**2
                n //= 10
            return ans
        
        slow = n
        fast = calc_next(n)
        while fast != 1 and slow != fast:
            slow = calc_next(slow)
            fast = calc_next(calc_next(fast))
        return fast == 1
# @lc code=end

