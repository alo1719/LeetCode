#
# @lc app=leetcode id=680 lang=python3
#
# [680] Valid Palindrome II
#
# https://leetcode.com/problems/valid-palindrome-ii/description/
#
# algorithms
# Easy (39.37%)
# Likes:    6317
# Dislikes: 328
# Total Accepted:    543.9K
# Total Submissions: 1.4M
# Testcase Example:  '"aba"'
#
# Given a string s, return true if the s can be palindrome after deleting at
# most one character from it.
# 
# 
# Example 1:
# 
# 
# Input: s = "aba"
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "abca"
# Output: true
# Explanation: You could delete the character 'c'.
# 
# 
# Example 3:
# 
# 
# Input: s = "abc"
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^5
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True
        for i in range(len(s)//2):
            if s[i] != s[-i-1]:
                dl = s[i+1:-i] if i > 0 else s[i+1:]
                dr = s[i:-i-1]
                print(dl, dr)
                return dl == dl[::-1] or dr == dr[::-1]

print(Solution.validPalindrome(None, "aba"))
print(Solution.validPalindrome(None, "abccb"))
print(Solution.validPalindrome(None, "abc"))
# @lc code=end

