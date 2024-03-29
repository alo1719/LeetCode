#
# @lc app=leetcode.cn id=1143 lang=python3
#
# [1143] Longest Common Subsequence
#
# https://leetcode.cn/problems/longest-common-subsequence/description/
#
# algorithms
# Medium (64.86%)
# Likes:    1162
# Dislikes: 0
# Total Accepted:    289.4K
# Total Submissions: 446.2K
# Testcase Example:  '"abcde"\n"ace"'
#
# Given two strings text1 and text2, return the length of their longest common
# subsequence. If there is no common subsequence, return 0.
# 
# A subsequence of a string is a new string generated from the original string
# with some characters (can be none) deleted without changing the relative
# order of the remaining characters.
# 
# 
# For example, "ace" is a subsequence of "abcde".
# 
# 
# A common subsequence of two strings is a subsequence that is common to both
# strings.
# 
# 
# Example 1:
# 
# 
# Input: text1 = "abcde", text2 = "ace" 
# Output: 3  
# Explanation: The longest common subsequence is "ace" and its length is 3.
# 
# 
# Example 2:
# 
# 
# Input: text1 = "abc", text2 = "abc"
# Output: 3
# Explanation: The longest common subsequence is "abc" and its length is 3.
# 
# 
# Example 3:
# 
# 
# Input: text1 = "abc", text2 = "def"
# Output: 0
# Explanation: There is no such common subsequence, so the result is 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= text1.length, text2.length <= 1000
# text1 and text2 consist of only lowercase English characters.
# 
# 
#

# @lc code=start
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # choose and not choose
        # 1. x and y
        # 2. not x and y
        # 3. x and not y
        # 4. not x and not y (1 and 4 can be merged)
        # f[i][j]: longest common subsequence of text1[:i] and text2[:j]
        # f[i][j] = max(f[i-1][j], f[i][j-1], f[i-1][j-1]+(s[i]==t[j]))
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                else:
                    dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1])
        return dp[-1][-1]
    
    def longestCommonSubstr(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0]*(n+1) for _ in range(m+1)]
        ans = 0
        for i in range(m):
            for j in range(n):
                if text1[i] == text2[j]:
                    dp[i+1][j+1] = dp[i][j]+1
                    ans = max(ans, dp[i+1][j+1])
                else:
                    dp[i+1][j+1] = 0
        return ans

# @lc code=end

print(Solution().longestCommonSubstr("abc", "aebec"))
print(Solution().longestCommonSubstr("abc", "aeabec"))