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
class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        visited.add(n)
        while True:
            n_str = str(n)
            new_number = 0
            for ch in n_str:
                new_number += int(ch) ** 2
            if new_number == 1: return True
            if new_number in visited: return False
            visited.add(new_number)
            n = new_number
# @lc code=end

