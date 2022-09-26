#
# @lc app=leetcode id=791 lang=python3
#
# [791] Custom Sort String
#
# https://leetcode.com/problems/custom-sort-string/description/
#
# algorithms
# Medium (69.41%)
# Likes:    2246
# Dislikes: 300
# Total Accepted:    197.9K
# Total Submissions: 285.1K
# Testcase Example:  '"cba"\n"abcd"'
#
# You are given two strings order and s. All the characters of order are unique
# and were sorted in some custom order previously.
#
# Permute the characters of s so that they match the order that order was
# sorted. More specifically, if a character x occurs before a character y in
# order, then x should occur before y in the permuted string.
#
# Return any permutation of s that satisfies this property.
#
#
# Example 1:
#
#
# Input: order = "cba", s = "abcd"
# Output: "cbad"
# Explanation:
# "a", "b", "c" appear in order, so the order of "a", "b", "c" should be "c",
# "b", and "a".
# Since "d" does not appear in order, it can be at any position in the returned
# string. "dcba", "cdba", "cbda" are also valid outputs.
#
#
# Example 2:
#
#
# Input: order = "cbafg", s = "abcd"
# Output: "cbad"
#
#
#
# Constraints:
#
#
# 1 <= order.length <= 26
# 1 <= s.length <= 200
# order and s consist of lowercase English letters.
# All the characters of order are unique.
#
#
#

# @lc code=start
class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order = {c: i for i, c in enumerate(order)}
        # print(order)
        # print(''.join(sorted(s, key=lambda c: order.get(c, -1))))
        return ''.join(sorted(s, key=lambda c: order.get(c, -1)))


Solution().customSortString("cba", "abcd")
Solution().customSortString("cbafg", "abcd")
# @lc code=end
