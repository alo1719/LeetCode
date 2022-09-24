#
# @lc app=leetcode id=387 lang=python3
#
# [387] First Unique Character in a String
#
# https://leetcode.com/problems/first-unique-character-in-a-string/description/
#
# algorithms
# Easy (58.72%)
# Likes:    6680
# Dislikes: 229
# Total Accepted:    1.2M
# Total Submissions: 2.1M
# Testcase Example:  '"leetcode"'
#
# Given a string s, find the first non-repeating character in it and return its
# index. If it does not exist, return -1.
#
#
# Example 1:
# Input: s = "leetcode"
# Output: 0
# Example 2:
# Input: s = "loveleetcode"
# Output: 2
# Example 3:
# Input: s = "aabb"
# Output: -1
#
#
# Constraints:
#
#
# 1 <= s.length <= 10^5
# s consists of only lowercase English letters.
#
#
#

# @lc code=start
class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        print(d)
        for k in d:
            if d[k] == 1:
                print(k)
                print(s.index(k))
                return s.index(k)
        return -1


Solution().firstUniqChar('leetcode')

# @lc code=end
