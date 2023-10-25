#
# @lc app=leetcode.cn id=712 lang=python3
#
# [712] Minimum ASCII Delete Sum for Two Strings
#
# https://leetcode.cn/problems/minimum-ascii-delete-sum-for-two-strings/description/
#
# algorithms
# Medium (68.99%)
# Likes:    337
# Dislikes: 0
# Total Accepted:    33.6K
# Total Submissions: 48.7K
# Testcase Example:  '"sea"\n"eat"'
#
# Given two strings s1 and s2, return the lowest ASCII sum of deleted
# characters to make two strings equal.
# 
# 
# Example 1:
# 
# 
# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the
# sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum
# possible to achieve this.
# 
# 
# Example 2:
# 
# 
# Input: s1 = "delete", s2 = "leet"
# Output: 403
# Explanation: Deleting "dee" from "delete" to turn the string into "let",
# adds 100[d] + 101[e] + 101[e] to the sum.
# Deleting "e" from "leet" adds 101[e] to the sum.
# At the end, both strings are equal to "let", and the answer is
# 100+101+101+101 = 403.
# If instead we turned both strings into "lee" or "eet", we would get answers
# of 433 or 417, which are higher.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s1.length, s2.length <= 1000
# s1 and s2 consist of lowercase English letters.
# 
# 
#

# @lc code=start
# TC: O(m*n)  SC: O(m*n)
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        # maximize LCS ascii value
        # f[i][j] = f[i-1][j-1]+s1[i] if s1[i] == s2[j]
        #         = max(f[i][j-1], f[i-1][j])
        @cache
        def f(i, j):
            if i == -1 or j == -1: return 0
            if s1[i] == s2[j]: return f(i-1, j-1)+ord(s1[i])
            else: return max(f(i, j-1), f(i-1, j))
        return sum(ord(x) for x in s1+s2)-2*f(len(s1)-1, len(s2)-1)
# @lc code=end

