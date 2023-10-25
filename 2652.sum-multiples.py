#
# @lc app=leetcode id=2652 lang=python3
#
# [2652] Sum Multiples
#
# https://leetcode.com/problems/sum-multiples/description/
#
# algorithms
# Easy (85.22%)
# Likes:    132
# Dislikes: 12
# Total Accepted:    27.5K
# Total Submissions: 32.2K
# Testcase Example:  '7'
#
# Given a positive integer n, find the sum of all integers in the range [1, n]
# inclusive that are divisible by 3, 5, or 7.
# 
# Return an integer denoting the sum of all numbers in the given range
# satisfying the constraint.
# 
# 
# Example 1:
# 
# 
# Input: n = 7
# Output: 21
# Explanation: Numbers in the range [1, 7] that are divisible by 3, 5, or 7 are
# 3, 5, 6, 7. The sum of these numbers is 21.
# 
# 
# Example 2:
# 
# 
# Input: n = 10
# Output: 40
# Explanation: Numbers in the range [1, 10] that are divisible by 3, 5, or 7
# are 3, 5, 6, 7, 9, 10. The sum of these numbers is 40.
# 
# 
# Example 3:
# 
# 
# Input: n = 9
# Output: 30
# Explanation: Numbers in the range [1, 9] that are divisible by 3, 5, or 7 are
# 3, 5, 6, 7, 9. The sum of these numbers is 30.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 10^3
# 
# 
#

# @lc code=start
class Solution:
    def sumOfMultiples(self, n: int) -> int:
        ans = 0
        for i in range(n+1):
            if i%3 == 0 or i%5 == 0 or i%7 == 0:
                ans += i
        return ans
# @lc code=end

