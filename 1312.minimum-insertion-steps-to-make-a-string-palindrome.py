#
# @lc app=leetcode.cn id=1312 lang=python3
#
# [1312] Minimum Insertion Steps to Make a String Palindrome
#
# https://leetcode.cn/problems/minimum-insertion-steps-to-make-a-string-palindrome/description/
#
# algorithms
# Hard (68.95%)
# Likes:    168
# Dislikes: 0
# Total Accepted:    21.7K
# Total Submissions: 31.5K
# Testcase Example:  '"zzazz"'
#
# Given a string s. In one step you can insert any character at any index of
# the string.
# 
# Return the minimum number of steps to make s palindrome.
# 
# A Palindrome String is one that reads the same backward as well as
# forward.
# 
# 
# Example 1:
# 
# 
# Input: s = "zzazz"
# Output: 0
# Explanation: The string "zzazz" is already palindrome we do not need any
# insertions.
# 
# 
# Example 2:
# 
# 
# Input: s = "mbadm"
# Output: 2
# Explanation: String can be "mbdadbm" or "mdbabdm".
# 
# 
# Example 3:
# 
# 
# Input: s = "leetcode"
# Output: 5
# Explanation: Inserting 5 characters the string becomes "leetcodocteel".
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def minInsertions(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)] # means s[i] to s[j] whether is palindrome
        for i in range(n-1, -1, -1):
            dp[i][i] = 1
            for j in range(i+1, n):
                if j == i+1 and s[i] == s[j]:
                    dp[i][j] = 2
                if dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = 2+dp[i+1][j-1]
                else:
                    dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1]) # without this is continuous palindrome
        return n-dp[0][-1]
# @lc code=end

