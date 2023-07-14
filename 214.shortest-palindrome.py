#
# @lc app=leetcode.cn id=214 lang=python3
#
# [214] Shortest Palindrome
#
# https://leetcode.cn/problems/shortest-palindrome/description/
#
# algorithms
# Hard (39.61%)
# Likes:    512
# Dislikes: 0
# Total Accepted:    44.1K
# Total Submissions: 111.2K
# Testcase Example:  '"aacecaaa"'
#
# You are given a string s. You can convert s to a palindrome by adding
# characters in front of it.
# 
# Return the shortest palindrome you can find by performing this
# transformation.
# 
# 
# Example 1:
# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:
# Input: s = "abcd"
# Output: "dcbabcd"
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of lowercase English letters only.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(1) if ignore the return string
class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # find the longest palindrome prefix
        # Rabin-karp
        p = 31
        m = 10**9+9
        p_pow = 1
        hashv = 0
        rhashv = 0
        lenn = 1
        for i, ch in enumerate(s):
            hashv = (hashv+(ord(ch)-ord('a')+1)*p_pow)%m
            rhashv = ((ord(ch)-ord('a')+1)+rhashv*p)%m
            p_pow = (p_pow*p)%m
            if hashv == rhashv:
                lenn = max(lenn, i+1)
        return s[lenn:][::-1]+s
# @lc code=end

