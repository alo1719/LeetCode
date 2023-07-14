#
# @lc app=leetcode.cn id=340 lang=python3
#
# [340] Longest Substring with At Most K Distinct Characters
#
# https://leetcode.cn/problems/longest-substring-with-at-most-k-distinct-characters/description/
#
# algorithms
# Medium (50.86%)
# Likes:    220
# Dislikes: 0
# Total Accepted:    23.4K
# Total Submissions: 46.1K
# Testcase Example:  '"eceba"\n2'
#
# Given a string s and an integer k, return the length of the longest substring
# of s that contains at most k distinct characters.
# 
# 
# Example 1:
# 
# 
# Input: s = "eceba", k = 2
# Output: 3
# Explanation: The substring is "ece" with length 3.
# 
# Example 2:
# 
# 
# Input: s = "aa", k = 1
# Output: 2
# Explanation: The substring is "aa" with length 2.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 5 * 10^4
# 0 <= k <= 50
# 
# 
#

# @lc code=start
from collections import defaultdict

# Sliding window
# TC: O(n)  SC: O(k)
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, ans, n = 0, 0, len(s)
        contain_dict = defaultdict(int)
        for right in range(n):
            contain_dict[s[right]] += 1
            while len(contain_dict) > k:
                contain_dict[s[left]] -= 1
                if contain_dict[s[left]] <= 0:
                    del contain_dict[s[left]]
                left += 1
            ans = max(ans, right-left+1)
        return ans
# @lc code=end

