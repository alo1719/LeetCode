#
# @lc app=leetcode.cn id=409 lang=python3
#
# [409] Longest Palindrome
#
# https://leetcode.cn/problems/longest-palindrome/description/
#
# algorithms
# Easy (55.77%)
# Likes:    544
# Dislikes: 0
# Total Accepted:    178.6K
# Total Submissions: 320.3K
# Testcase Example:  '"abccccdd"'
#
# Given a string s which consists of lowercase or uppercase letters, return the
# length of the longest palindrome that can be built with those letters.
# 
# Letters are case sensitive, for example, "Aa" is not considered a palindrome
# here.
# 
# 
# Example 1:
# 
# 
# Input: s = "abccccdd"
# Output: 7
# Explanation: One longest palindrome that can be built is "dccaccd", whose
# length is 7.
# 
# 
# Example 2:
# 
# 
# Input: s = "a"
# Output: 1
# Explanation: The longest palindrome that can be built is "a", whose length is
# 1.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 2000
# s consists of lowercase and/or uppercase English letters only.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def longestPalindrome(self, s: str) -> int:
        c = Counter(s)
        ans = 0
        has_odd = False
        for v in c.values():
            ans += v//2*2
            if v%2 == 1:
                has_odd = True
        return ans+1 if has_odd else ans
# @lc code=end

