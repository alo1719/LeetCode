#
# @lc app=leetcode id=2062 lang=python3
#
# [2062] Count Vowel Substrings of a String
#
# https://leetcode.com/problems/count-vowel-substrings-of-a-string/description/
#
# algorithms
# Easy (66.05%)
# Likes:    757
# Dislikes: 181
# Total Accepted:    28.5K
# Total Submissions: 43.2K
# Testcase Example:  '"aeiouu"'
#
# A substring is a contiguous (non-empty) sequence of characters within a
# string.
# 
# A vowel substring is a substring that only consists of vowels ('a', 'e', 'i',
# 'o', and 'u') and has all five vowels present in it.
# 
# Given a string word, return the number of vowel substrings in word.
# 
# 
# Example 1:
# 
# 
# Input: word = "aeiouu"
# Output: 2
# Explanation: The vowel substrings of word are as follows (underlined):
# - "aeiouu"
# - "aeiouu"
# 
# 
# Example 2:
# 
# 
# Input: word = "unicornarihan"
# Output: 0
# Explanation: Not all 5 vowels are present, so there are no vowel
# substrings.
# 
# 
# Example 3:
# 
# 
# Input: word = "cuaieuouac"
# Output: 7
# Explanation: The vowel substrings of word are as follows (underlined):
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# - "cuaieuouac"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 100
# word consists of lowercase English letters only.
# 
# 
#

# @lc code=start
# Snowflake OA
class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans, last_consonant = 0, -1
        last_seen_vowels = {v: -1 for v in "aeiou"}
        for i, x in enumerate(word):
            if x in last_seen_vowels:
                last_seen_vowels[x] = i
                ans += max(min(last_seen_vowels.values()) - last_consonant, 0)
            else:
                last_consonant = i
        return ans
# @lc code=end

