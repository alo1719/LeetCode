#
# @lc app=leetcode id=125 lang=python3
#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (43.28%)
# Likes:    4901
# Dislikes: 6008
# Total Accepted:    1.6M
# Total Submissions: 3.6M
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# A phrase is a palindrome if, after converting all uppercase letters into
# lowercase letters and removing all non-alphanumeric characters, it reads the
# same forward and backward. Alphanumeric characters include letters and
# numbers.
#
# Given a string s, return true if it is a palindrome, or false otherwise.
#
#
# Example 1:
#
#
# Input: s = "A man, a plan, a canal: Panama"
# Output: true
# Explanation: "amanaplanacanalpanama" is a palindrome.
#
#
# Example 2:
#
#
# Input: s = "race a car"
# Output: false
# Explanation: "raceacar" is not a palindrome.
#
#
# Example 3:
#
#
# Input: s = " "
# Output: true
# Explanation: s is an empty string "" after removing non-alphanumeric
# characters.
# Since an empty string reads the same forward and backward, it is a
# palindrome.
#
#
#
# Constraints:
#
#
# 1 <= s.length <= 2 * 10^5
# s consists only of printable ASCII characters.
#
#
#

# @lc code=start
# TC: O(n)  SC: O(1)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        i, j = -1, n
        while True:
            i += 1
            j -= 1
            while i+1 < n and not s[i].isalnum():
                i += 1
            while j-1 >= 0 and not s[j].isalnum():
                j -= 1
            if i >= j: return True
            if s[i].lower() != s[j].lower(): return False
# @lc code=end
