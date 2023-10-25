#
# @lc app=leetcode.cn id=664 lang=python3
#
# [664] Strange Printer
#
# https://leetcode.cn/problems/strange-printer/description/
#
# algorithms
# Hard (65.28%)
# Likes:    316
# Dislikes: 0
# Total Accepted:    27.5K
# Total Submissions: 42.1K
# Testcase Example:  '"aaabbb"'
#
# There is a strange printer with the following two special properties:
# 
# 
# The printer can only print a sequence of the same character each time.
# At each turn, the printer can print new characters starting from and ending
# at any place and will cover the original existing characters.
# 
# 
# Given a string s, return the minimum number of turns the printer needed to
# print it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aaabbb"
# Output: 2
# Explanation: Print "aaa" first and then print "bbb".
# 
# 
# Example 2:
# 
# 
# Input: s = "aba"
# Output: 2
# Explanation: Print "aaa" first and then print "b" from the second place of
# the string, which will cover the existing character 'a'.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
# TC: O(n^3)  SC: O(n^2)
class Solution:
    def strangePrinter(self, s: str) -> int:
        # f[i][j]: min turns to print s[i..j]
        # f[i][j] = f[i][j-1] if s[i] == s[j]
        #         = min(f[i][k]+f[k+1][j] for k in [i..j-1])
        @cache
        def f(i, j):
            if i == j: return 1
            if s[i] == s[j]: return f(i, j-1)
            else:
                ans = inf
                for k in range(i, j):
                    ans = min(ans, f(i, k)+f(k+1, j))
                return ans
        return f(0, len(s)-1)
# @lc code=end

