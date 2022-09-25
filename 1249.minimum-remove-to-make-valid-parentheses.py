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

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # len(s)>=1
        left = 0
        res = []
        res2 = []
        for c in s:
            if c=='(':
                left+=1
                res.append(c)
            elif c==')':
                if left > 0:
                    left -= 1
                    res.append(c)
            else:
                res.append(c)
        print(res)
        res.reverse()
        right = 0
        for c in res:
            if c==')':
                right+=1
                res2.append(c)
            elif c=='(':
                if right > 0:
                    right -=1
                    res2.append(c)
            else:
                res2.append(c)
        res2.reverse()
        print(res2)
        return "".join(res2)



Solution.minRemoveToMakeValid(None, "lee(t(c)o)de)")
Solution.minRemoveToMakeValid(None, "a)b(c)d")
Solution.minRemoveToMakeValid(None, "))((")
Solution.minRemoveToMakeValid(None, "(a(b))")

# @lc code=end

