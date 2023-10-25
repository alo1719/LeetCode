#
# @lc app=leetcode.cn id=2745 lang=python3
#
# [2745] Construct the Longest New String
#
# https://leetcode.cn/problems/construct-the-longest-new-string/description/
#
# algorithms
# Medium (57.45%)
# Likes:    10
# Dislikes: 0
# Total Accepted:    3.1K
# Total Submissions: 5.4K
# Testcase Example:  '2\n5\n1'
#
# You are given three integers x, y, and z.
# 
# You have x strings equal to "AA", y strings equal to "BB", and z strings
# equal to "AB". You want to choose some (possibly all or none) of these
# strings and concactenate them in some order to form a new string. This new
# string must not contain "AAA" or "BBB" as a substring.
# 
# Return the maximum possible length of the new string.
# 
# A substring is a contiguous non-empty sequence of characters within a
# string.
# 
# 
# Example 1:
# 
# 
# Input: x = 2, y = 5, z = 1
# Output: 12
# Explanation: We can concactenate the strings "BB", "AA", "BB", "AA", "BB",
# and "AB" in that order. Then, our new string is "BBAABBAABBAB". 
# That string has length 12, and we can show that it is impossible to construct
# a string of longer length.
# 
# 
# Example 2:
# 
# 
# Input: x = 3, y = 2, z = 2
# Output: 14
# Explanation: We can concactenate the strings "AB", "AB", "AA", "BB", "AA",
# "BB", and "AA" in that order. Then, our new string is "ABABAABBAABBAA". 
# That string has length 14, and we can show that it is impossible to construct
# a string of longer length.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= x, y, z <= 50
# 
# 
#

# @lc code=start
class Solution:
    def longestString(self, x: int, y: int, z: int) -> int:
        @cache
        def f(x, y, z, last):
            if x < 0 or y < 0 or z < 0: return 0
            if last == 'AA' and y == 0: return 0
            if last == 'BB' and x == 0 and z == 0: return 0
            if last == 'AB' and x == 0 and z == 0: return 0
            if last == 'AA':
                return 2+f(x, y-1, z, 'BB')
            if last == 'BB':
                return max(f(x-1, y, z, 'AA'), f(x, y, z-1, 'AB'))+2
            if last == 'AB':
                return max(f(x-1, y, z, 'AA'), f(x, y, z-1, 'AB'))+2
            
        return max(f(x-1, y, z, 'AA'), f(x, y-1, z,'BB'), f(x, y, z-1, 'AB'))+2
# @lc code=end

