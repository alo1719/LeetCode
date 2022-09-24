#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (40.75%)
# Likes:    15766
# Dislikes: 782
# Total Accepted:    2.7M
# Total Submissions: 6.6M
# Testcase Example:  '"()"'
#
# Given a string s containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.
#
#
#
# Example 1:
#
#
# Input: s = "()"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: s = "(]"
# Output: false
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^4
# s consists of parentheses only '()[]{}'.
#
#
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        for c in s:
            if c == '(' or c == '[' or c == '{':
                a.append(c)
            elif c == ')':
                if a and a[-1] == '(':
                    a.pop()
                else:
                    return False
            elif c == ']':
                if a and a[-1] == '[':
                    a.pop()
                else:
                    return False
            elif c == '}':
                if a and a[-1] == '{':
                    a.pop()
                else:
                    return False
        return not a
# @lc code=end
