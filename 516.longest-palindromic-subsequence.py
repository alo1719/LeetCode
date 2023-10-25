#
# @lc app=leetcode.cn id=516 lang=python3
#
# [516] Longest Palindromic Subsequence
#
# https://leetcode.cn/problems/longest-palindromic-subsequence/description/
#
# algorithms
# Medium (67.16%)
# Likes:    1083
# Dislikes: 0
# Total Accepted:    191.7K
# Total Submissions: 285.4K
# Testcase Example:  '"bbbab"'
#
# Given a string s, find the longest palindromic subsequence's length in s.
# 
# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining
# elements.
# 
# 
# Example 1:
# 
# 
# Input: s = "bbbab"
# Output: 4
# Explanation: One possible longest palindromic subsequence is "bbbb".
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: 2
# Explanation: One possible longest palindromic subsequence is "bb".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consists only of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # f[i][j] = f[i+1][j-1]+2 if s[i]==s[j] else max(f[i+1][j], f[i][j-1])
# @lc code=end

