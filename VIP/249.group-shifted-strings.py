#
# @lc app=leetcode.cn id=249 lang=python3
#
# [249] Group Shifted Strings
#
# https://leetcode.cn/problems/group-shifted-strings/description/
#
# algorithms
# Medium (64.83%)
# Likes:    97
# Dislikes: 0
# Total Accepted:    9.8K
# Total Submissions: 15K
# Testcase Example:  '["abc","bcd","acef","xyz","az","ba","a","z"]'
#
# We can shift a string by shifting each of its letters to its successive
# letter.
# 
# 
# For example, "abc" can be shifted to be "bcd".
# 
# 
# We can keep shifting the string to form a sequence.
# 
# 
# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd"
# -> ... -> "xyz".
# 
# 
# Given an array of strings strings, group all strings[i] that belong to the
# same shifting sequence. You may return the answer in any order.
# 
# 
# Example 1:
# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
# Example 2:
# Input: strings = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
from typing import List
from collections import defaultdict


# TC: O(nl)  SC: O(n)
class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dict = defaultdict(list)
        for string in strings:
            offsets = str([(ord(ch)-ord(string[0])+26) % 26 for ch in string])
            dict[offsets].append(string)
        return list(dict.values())


print(Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]))
print(Solution().groupStrings(["a"]))
# @lc code=end
