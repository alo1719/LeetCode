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
# TC: O(n)  SC: O(len(set(s))
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        c = Counter()
        n = len(s)
        ans = left = 0
        for right in range(n):  # [left, right]
            c[s[right]] += 1
            while c[s[right]] > 1:
                c[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans

        # DP
        # f[i] = min(f[i-1]+1, i-d[s[i]] if s[i] in d else inf), while updating d[s[i]] = i
        if not s: return 0
        n = len(s)
        d = {}
        f = [0]*n
        for i in range(n):
            if s[i] in d:
                f[i] = min(f[i-1]+1, i-d[s[i]])
            else:
                f[i] = f[i-1]+1
            d[s[i]] = i
        return max(f)
# @lc code=end

