#
# @lc app=leetcode id=227 lang=python3
#
# [227] Basic Calculator II
#
# https://leetcode.com/problems/basic-calculator-ii/description/
#
# algorithms
# Medium (42.09%)
# Likes:    4875
# Dislikes: 632
# Total Accepted:    473K
# Total Submissions: 1.1M
# Testcase Example:  '"3+2*2"'
#
# Given a string s which represents an expression, evaluate this expression and
# return its value. 
# 
# The integer division should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# Input: s = "3+2*2"
# Output: 7
# Example 2:
# Input: s = " 3/2 "
# Output: 1
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 3 * 10^5
# s consists of integers and operators ('+', '-', '*', '/') separated by some
# number of spaces.
# s represents a valid expression.
# All the integers in the expression are non-negative integers in the range [0,
# 2^31 - 1].
# The answer is guaranteed to fit in a 32-bit integer.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def calculate(self, s: str) -> int:
        nums, ops = [], []
        n, i = len(s), 0
        priority = {"(":0, "+":1, "-":1, "*":2, "/":2}  # only calc when ops[-1] is higher than current op
        while i < n:
            if s[i].isdigit():
                j = i
                while i+1 < n and s[i+1].isdigit(): i += 1
                nums.append(int(s[j:i+1]))
            elif s[i] in '+-*/':  # + - * /
                while ops and priority[ops[-1]] >= priority[s[i]]:
                    self.calc(nums, ops)
                ops.append(s[i])
            i += 1

        while ops:
            self.calc(nums, ops)
        return nums[-1]


    def calc(self, nums, ops):
        B = nums.pop()
        A = nums.pop()
        op = ops.pop()
        nums.append(self.calc_num(op, A, B))
    
    def calc_num(self, op, A, B):
        if op == "+":
            return A+B
        if op == "-":
            return A-B
        if op == "*":
            return A*B
        if op == "/":
            return int(A/B)  # truncate toward zero

Solution().calculate("3+2*2")
Solution().calculate(" 3/2 ")
Solution().calculate(" 3+5 / 2 ")
# @lc code=end

