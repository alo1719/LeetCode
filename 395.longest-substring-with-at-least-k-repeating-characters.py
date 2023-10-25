#
# @lc app=leetcode.cn id=395 lang=python3
#
# [395] Longest Substring with At Least K Repeating Characters
#
# https://leetcode.cn/problems/longest-substring-with-at-least-k-repeating-characters/description/
#
# algorithms
# Medium (52.48%)
# Likes:    838
# Dislikes: 0
# Total Accepted:    86.1K
# Total Submissions: 164.1K
# Testcase Example:  '"aaabb"\n3'
#
# Given a string s and an integer k, return the length of the longest substring
# of s such that the frequency of each character in this substring is greater
# than or equal to k.
# 
# if no such substring exists, return 0.
# 
# 
# Example 1:
# 
# 
# Input: s = "aaabb", k = 3
# Output: 3
# Explanation: The longest substring is "aaa", as 'a' is repeated 3 times.
# 
# 
# Example 2:
# 
# 
# Input: s = "ababbc", k = 2
# Output: 5
# Explanation: The longest substring is "ababb", as 'a' is repeated 2 times and
# 'b' is repeated 3 times.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 10^4
# s consists of only lowercase English letters.
# 1 <= k <= 10^5
# 
# 
#

# @lc code=start
# TC: O(26n)  SC: O(n)
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        if len(s) < k: return 0
        cnt = Counter(s)
        for ch in cnt:
            if cnt[ch] < k:
                return max(self.longestSubstring(sub_s, k) for sub_s in s.split(ch))
        return len(s)
# @lc code=end

