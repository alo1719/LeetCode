#
# @lc app=leetcode id=2645 lang=python3
#
# [2645] Minimum Additions to Make Valid String
#
# https://leetcode.com/problems/minimum-additions-to-make-valid-string/description/
#
# algorithms
# Medium (49.19%)
# Likes:    346
# Dislikes: 12
# Total Accepted:    17.8K
# Total Submissions: 36.2K
# Testcase Example:  '"b"'
#
# Given a string word to which you can insert letters "a", "b" or "c" anywhere
# and any number of times, return the minimum number of letters that must be
# inserted so that word becomes valid.
# 
# A string is called valid if it can be formed by concatenating the string
# "abc" several times.
# 
# 
# Example 1:
# 
# 
# Input: word = "b"
# Output: 2
# Explanation: Insert the letter "a" right before "b", and the letter "c" right
# next to "a" to obtain the valid string "abc".
# 
# 
# Example 2:
# 
# 
# Input: word = "aaa"
# Output: 6
# Explanation: Insert letters "b" and "c" next to each "a" to obtain the valid
# string "abcabcabc".
# 
# 
# Example 3:
# 
# 
# Input: word = "abc"
# Output: 0
# Explanation: word is already valid. No modifications are needed. 
# 
# 
# 
# Constraints:
# 
# 
# 1 <= word.length <= 50
# word consists of letters "a", "b" and "c" only. 
# 
# 
#

# @lc code=start
class Solution:
    def addMinimum(self, word: str) -> int:
        word = word.replace('abc', 'xxx')
        ans = word.count('ab')
        word = word.replace('ab', 'xx')
        ans += word.count('bc')
        word = word.replace('bc', 'xx')
        ans += word.count('ac')
        word = word.replace('ac', 'xx')
        ans += (word.count('a')+word.count('b')+word.count('c'))*2
        return ans
# @lc code=end

