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
        num_stk = []
        opt_stk = []
        n = len(s)
        i = 0
        priority = {"(":0, "+":1, "-":1, "*":2, "/":2}
        while i < n:
            if "0" <= s[i] <= "9":
                j = i
                while i+1 < n and "0" <= s[i+1] <= "9":
                    i += 1
                num_stk.append(int(s[j:i+1]))
            elif s[i] == "(":
                opt_stk.append("(")
            elif s[i] == ")":
                while opt_stk[-1] != "(":
                    self.calc(num_stk, opt_stk)
                opt_stk.pop()
            else:  # + - * /
                while opt_stk and priority[opt_stk[-1]] >= priority[s[i]]:
                    self.calc(num_stk, opt_stk)  # respect to priority
                opt_stk.append(s[i])
            i += 1

        while opt_stk:
            self.calc(num_stk, opt_stk)
        
        return num_stk[-1]

    
    def calc(self, num_stk, opt_stk):
        B = num_stk.pop()
        A = num_stk.pop()
        opt = opt_stk.pop()
        num_stk.append(self.calc_num(opt, A, B))
    
    def calc_num(self, opt, A, B):
        if opt == "+":
            return A+B
        if opt == "-":
            return A-B
        if opt == "*":
            return A*B
        if opt == "/":
            return int(A/B)  # truncate toward zero
# @lc code=end

