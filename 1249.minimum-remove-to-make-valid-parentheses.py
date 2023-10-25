#
# @lc app=leetcode id=1249 lang=python3
#
# [1249] Minimum Remove to Make Valid Parentheses
#
# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/description/
#
# algorithms
# Medium (65.63%)
# Likes:    5289
# Dislikes: 99
# Total Accepted:    467.8K
# Total Submissions: 712.9K
# Testcase Example:  '"lee(t(c)o)de)"'
#
# Given a string s of '(' , ')' and lowercase English characters.
# 
# Your task is to remove the minimum number of parentheses ( '(' or ')', in any
# positions ) so that the resulting parentheses string is valid and return any
# valid string.
# 
# Formally, a parentheses string is valid if and only if:
# 
# 
# It is the empty string, contains only lowercase characters, or
# It can be written as AB (A concatenated with B), where A and B are valid
# strings, or
# It can be written as (A), where A is a valid string.
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "lee(t(c)o)de)"
# Output: "lee(t(c)o)de"
# Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.
# 
# 
# Example 2:
# 
# 
# Input: s = "a)b(c)d"
# Output: "ab(c)d"
# 
# 
# Example 3:
# 
# 
# Input: s = "))(("
# Output: ""
# Explanation: An empty string is also valid.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s[i] is either'(' , ')', or lowercase English letter.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(1)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        ans = ''
        left, right = 0, s.count(')')
        for ch in s:
            if ch == '(':
                if right > 0:
                    ans += ch
                    left += 1
                    right -= 1
            elif ch == ')':
                if left > 0:
                    ans += ch
                    left -= 1
                else:
                    right -= 1
            else:
                ans += ch
        return ans


Solution.minRemoveToMakeValid(None, "lee(t(c)o)de)")
Solution.minRemoveToMakeValid(None, "a)b(c)d")
Solution.minRemoveToMakeValid(None, "))((")
Solution.minRemoveToMakeValid(None, "(a(b))")

# @lc code=end

