#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# https://leetcode.com/problems/longest-common-prefix/description/
#
# algorithms
# Easy (40.56%)
# Likes:    10427
# Dislikes: 3394
# Total Accepted:    1.9M
# Total Submissions: 4.6M
# Testcase Example:  '["flower","flow","flight"]'
#
# Write a function to find the longest common prefix string amongst an array of
# strings.
#
# If there is no common prefix, return an empty string "".
#
#
# Example 1:
#
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
#
#
# Example 2:
#
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
#
# Constraints:
#
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.
#
#
#

# @lc code=start
from typing import List

# TC: O(nm)  SC: O(1), m is the length of the string
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ''
        min_len = min([len(s) for s in strs])
        n = len(strs)
        for i in range(min_len):
            cur = strs[0][i]
            for j in range(n):
                if strs[j][i] != cur:
                    return ans
            ans += cur
        return ans

# @lc code=end
