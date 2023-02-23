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
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        left, right, ans, n = 0, -1, 0, len(s)
        contain_dict = defaultdict(int)
        for left in range(n):
            if left >= 1:
                contain_dict[s[left-1]] -= 1
                if contain_dict[s[left-1]] <= 0:
                    del contain_dict[s[left-1]]
            while right + 1 < n and (len(contain_dict) < k or s[right + 1] in contain_dict):
                right += 1
                contain_dict[s[right]] += 1
                ans = max(ans, right-left+1)
        return ans
# @lc code=end

