#
# @lc app=leetcode.cn id=383 lang=python3
#
# [383] Ransom Note
#
# https://leetcode.cn/problems/ransom-note/description/
#
# algorithms
# Easy (60.82%)
# Likes:    762
# Dislikes: 0
# Total Accepted:    359.2K
# Total Submissions: 590.3K
# Testcase Example:  '"a"\n"b"'
#
# Given two strings ransomNote and magazine, return true if ransomNote can be
# constructed by using the letters from magazine and false otherwise.
# 
# Each letter in magazine can only be used once in ransomNote.
# 
# 
# Example 1:
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
# Input: ransomNote = "aa", magazine = "aab"
# Output: true
# 
# 
# Constraints:
# 
# 
# 1 <= ransomNote.length, magazine.length <= 10^5
# ransomNote and magazine consist of lowercase English letters.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        c1 = Counter(ransomNote)
        c2 = Counter(magazine)
        for k in c1:
            if c1[k] > c2[k]:
                return False
        return True
# @lc code=end

