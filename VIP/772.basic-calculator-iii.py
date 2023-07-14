#
# @lc app=leetcode.cn id=772 lang=python3
#
# [772] Basic Calculator III
#
# https://leetcode.cn/problems/basic-calculator-iii/description/
#
# algorithms
# Hard (53.06%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    12K
# Total Submissions: 22.6K
# Testcase Example:  '"1+1"'
#
# Implement a basic calculator to evaluate a simple expression string.
# 
# The expression string contains only non-negative integers, '+', '-', '*', '/'
# operators, and open '(' and closing parentheses ')'. The integer division
# should truncate toward zero.
# 
# You may assume that the given expression is always valid. All intermediate
# results will be in the range of [-2^31, 2^31 - 1].
# 
# Note: You are not allowed to use any built-in function which evaluates
# strings as mathematical expressions, such as eval().
# 
# 
# Example 1:
# 
# 
# Input: s = "1+1"
# Output: 2
# 
# 
# Example 2:
# 
# 
# Input: s = "6-4/2"
# Output: 4
# 
# 
# Example 3:
# 
# 
# Input: s = "2*(5+5*2)/3+(6/2+8)"
# Output: 21
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s <= 10^4
# s consists of digits, '+', '-', '*', '/', '(', and ')'.
# s is a valid expression.
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
            elif s[i] == "(":
                ops.append("(")
            elif s[i] == ")":
                while ops[-1] != "(":
                    self.calc(nums, ops)
                ops.pop()
            else:  # + - * /
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
# @lc code=end

