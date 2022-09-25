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
class Solution:
    def calculate(self, s: str) -> int:
        numbers = []
        ops = []
        i = 0
        while i < len(s):
            if s[i] in '+-*/':
                ops.append(s[i])
                i += 1
            elif s[i] == ' ':
                i += 1
            else:
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                numbers.append(num)
        print(numbers, ops)
        i = 0
        while i < len(ops):
            if ops[i] == '*':
                numbers[i] *= numbers[i+1]
                numbers.pop(i+1)
                ops.pop(i)
                print(numbers, ops)
            elif ops[i] == '/':
                numbers[i] //= numbers[i+1]
                numbers.pop(i+1)
                ops.pop(i)
            else:
                i += 1
        print(numbers, ops)
        i = 0
        while i < len(ops):
            if ops[i] == '+':
                numbers[i] += numbers[i+1]
                numbers.pop(i+1)
                ops.pop(i)
            elif ops[i] == '-':
                numbers[i] -= numbers[i+1]
                numbers.pop(i+1)
                ops.pop(i)
            else:
                i += 1
        print(numbers, ops)
        print(numbers[0])
        return numbers[0]

Solution().calculate("3+2*2")
Solution().calculate(" 3/2 ")
Solution().calculate(" 3+5 / 2 ")
# @lc code=end

