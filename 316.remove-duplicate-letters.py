#
# @lc app=leetcode.cn id=316 lang=python3
#
# [316] Remove Duplicate Letters
#
# https://leetcode.cn/problems/remove-duplicate-letters/description/
#
# algorithms
# Medium (48.37%)
# Likes:    975
# Dislikes: 0
# Total Accepted:    122.4K
# Total Submissions: 252.9K
# Testcase Example:  '"bcabc"'
#
# Given a string s, remove duplicate letters so that every letter appears once
# and only once. You must make sure your result is the smallest in
# lexicographical order among all possible results.
# 
# 
# Example 1:
# 
# 
# Input: s = "bcabc"
# Output: "abc"
# 
# 
# Example 2:
# 
# 
# Input: s = "cbacdcbc"
# Output: "acdb"
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
# Note: This question is the same as 1081:
# https://leetcode.com/problems/smallest-subsequence-of-distinct-characters/
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        cnt = Counter(s)
        stk = []
        in_stk = set()
        for ch in s:
            cnt[ch] -= 1
            if ch in in_stk: continue
            while stk and stk[-1] > ch and cnt[stk[-1]] > 0:
                in_stk.remove(stk.pop())
            stk.append(ch)
            in_stk.add(ch)
        return ''.join(stk)
# @lc code=end

