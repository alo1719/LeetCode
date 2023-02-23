#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.cn/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (39.09%)
# Likes:    8617
# Dislikes: 0
# Total Accepted:    2.1M
# Total Submissions: 5.5M
# Testcase Example:  '"abcabcbb"'
#
# Given a string s, find the length of the longest substring without repeating
# characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# 
# 
# Example 2:
# 
# 
# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# 
# 
# Example 3:
# 
# 
# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a
# substring.
# 
# 
# 
# Constraints:
# 
# 
# 0 <= s.length <= 5 * 10^4
# s consists of English letters, digits, symbols and spaces.
# 
# 
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        char_set = set()
        # right = -1 means take nothing, result is [left, right]
        right, ans = -1, 0
        n = len(s)
        for left in range(n):
            if left != 0:
                char_set.remove(s[left - 1])
            while right + 1 <= n - 1 and s[right + 1] not in char_set:
                char_set.add(s[right + 1])
                right += 1
                ans = max(ans, right - left + 1)
        return ans
# @lc code=end

