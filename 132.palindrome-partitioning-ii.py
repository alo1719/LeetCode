#
# @lc app=leetcode.cn id=132 lang=python3
#
# [132] Palindrome Partitioning II
#
# https://leetcode.cn/problems/palindrome-partitioning-ii/description/
#
# algorithms
# Hard (49.88%)
# Likes:    648
# Dislikes: 0
# Total Accepted:    72.5K
# Total Submissions: 145.4K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome.
# 
# Return the minimum cuts needed for a palindrome partitioning of s.
# 
# 
# Example 1:
# 
# 
# Input: s = "aab"
# Output: 1 
# Explanation: The palindrome partitioning ["aa","b"] could be produced using 1
# cut.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 0
# 
# 
# Example 3:
# 
# 
# Input: s = "ab"
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase English letters only.
# 
# 
#

# @lc code=start
# TC: O(n^2)  SC: O(n^2)
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        # same as LC5
        dp = [[False]*n for _ in range(n)]  # means s[i] to s[j] whether is palindrome
        for i in range(n-1, -1, -1):
            dp[i][i] = True
            for j in range(i+1, n):
                if (j == i+1 and s[i] == s[j]) or (dp[i+1][j-1] and s[i] == s[j]):
                    dp[i][j] = True
        f = [0]*n  # f[i] means [0, i] min cut num, f[i] = min(f[j-1]+1 if dp[j][i])
        for i in range(n):
            if dp[0][i]: f[i] = 0
            else:
                f[i] = i
                for j in range(i+1):  # enumerate cut point
                    if dp[j][i]: f[i] = min(f[i], f[j-1]+1)
        return f[-1]
# @lc code=end

