#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] Longest Palindromic Substring
#
# https://leetcode.cn/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (37.35%)
# Likes:    6065
# Dislikes: 0
# Total Accepted:    1.3M
# Total Submissions: 3.5M
# Testcase Example:  '"babad"'
#
# Given a string s, return the longest palindromic substring in s.
# 
# 
# Example 1:
# 
# 
# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: s = "cbbd"
# Output: "bb"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 1000
# s consist of only digits and English letters.
# 
# 
#

# @lc code=start
# Palindrome DP
class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Can also use center expansion, TC O(n^2), SC O(1)
        # Can use Rabin-Karp and binary search to optimize center expansion, TC O(nlogn), SC O(n)
        # The ultimate answer is Manacher, TC O(n), SC O(n)
        ans, max, n = s[0], 1, len(s)
        dp = [[False for _ in range(n)] for _ in range(n)] # means s[i] to s[j] whether is palindrome
        for i in range(n - 1, -1, -1):
            dp[i][i] = True
            for j in range(i + 1, n):
                if (j == i+1 and s[i] == s[j]) or (dp[i+1][j-1] and s[i] == s[j]):
                    dp[i][j] = True
                    if j-i+1 > max:
                        max = j-i+1
                        ans = s[i:j+1]
        return ans
# @lc code=end

