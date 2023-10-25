#
# @lc app=leetcode id=2272 lang=python3
#
# [2272] Substring With Largest Variance
#
# https://leetcode.com/problems/substring-with-largest-variance/description/
#
# algorithms
# Hard (36.83%)
# Likes:    1674
# Dislikes: 189
# Total Accepted:    60.3K
# Total Submissions: 127.1K
# Testcase Example:  '"aababbb"'
#
# The variance of a string is defined as the largest difference between the
# number of occurrences of any 2 characters present in the string. Note the two
# characters may or may not be the same.
# 
# Given a string s consisting of lowercase English letters only, return the
# largest variance possible among all substrings of s.
# 
# A substring is a contiguous sequence of characters within a string.
# 
# 
# Example 1:
# 
# 
# Input: s = "aababbb"
# Output: 3
# Explanation:
# All possible variances along with their respective substrings are listed
# below:
# - Variance 0 for substrings "a", "aa", "ab", "abab", "aababb", "ba", "b",
# "bb", and "bbb".
# - Variance 1 for substrings "aab", "aba", "abb", "aabab", "ababb", "aababbb",
# and "bab".
# - Variance 2 for substrings "aaba", "ababbb", "abbb", and "babb".
# - Variance 3 for substring "babbb".
# Since the largest possible variance is 3, we return it.
# 
# 
# Example 2:
# 
# 
# Input: s = "abcde"
# Output: 0
# Explanation:
# No letter occurs more than once in s, so the variance of every substring is
# 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def largestVariance(self, s: str) -> int:
        alphabet = set(s)
        n = len(s)
        ans = 0
        for a, b in permutations(alphabet, 2):
            diff = 0
            diff_has_b = -inf
            for i in range(n):
                if s[i] == a:
                    diff += 1
                    diff_has_b += 1
                if s[i] == b:
                    diff -= 1
                    diff_has_b = diff  # diff is valid until reach b
                    diff = max(0, diff)
                ans = max(ans, diff_has_b)
        return ans
# @lc code=end

