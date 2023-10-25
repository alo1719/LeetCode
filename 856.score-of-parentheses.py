#
# @lc app=leetcode.cn id=856 lang=python3
#
# [856] Score of Parentheses
#
# https://leetcode.cn/problems/score-of-parentheses/description/
#
# algorithms
# Medium (68.43%)
# Likes:    490
# Dislikes: 0
# Total Accepted:    54.4K
# Total Submissions: 79.5K
# Testcase Example:  '"()"'
#
# Given a balanced parentheses string s, return the score of the string.
# 
# The score of a balanced parentheses string is based on the following
# rule:
# 
# 
# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "()"
# Output: 1
# 
# 
# Example 2:
# 
# 
# Input: s = "(())"
# Output: 2
# 
# 
# Example 3:
# 
# 
# Input: s = "()()"
# Output: 2
# 
# 
# 
# Constraints:
# 
# 
# 2 <= s.length <= 50
# s consists of only '(' and ')'.
# s is a balanced parentheses string.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stk = []
        ans = 0
        for ch in s:
            if ch == '(':
                stk.append(0)
            else:
                top = stk.pop()
                if top == 0: res = 1
                else: res = top*2
                if stk: stk[-1] += res
                else: ans += res
        return ans
# @lc code=end

