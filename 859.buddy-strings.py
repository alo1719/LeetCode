#
# @lc app=leetcode id=859 lang=python3
#
# [859] Buddy Strings
#
# https://leetcode.com/problems/buddy-strings/description/
#
# algorithms
# Easy (29.22%)
# Likes:    1861
# Dislikes: 1163
# Total Accepted:    149.5K
# Total Submissions: 511.2K
# Testcase Example:  '"ab"\n"ba"'
#
# Given two strings s and goal, return true if you can swap two letters in s so
# the result is equal to goal, otherwise, return false.
# 
# Swapping letters is defined as taking two indices i and j (0-indexed) such
# that i != j and swapping the characters at s[i] and s[j].
# 
# 
# For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
# 
# 
# 
# Example 1:
# 
# 
# Input: s = "ab", goal = "ba"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is
# equal to goal.
# 
# 
# Example 2:
# 
# 
# Input: s = "ab", goal = "ab"
# Output: false
# Explanation: The only letters you can swap are s[0] = 'a' and s[1] = 'b',
# which results in "ba" != goal.
# 
# 
# Example 3:
# 
# 
# Input: s = "aa", goal = "aa"
# Output: true
# Explanation: You can swap s[0] = 'a' and s[1] = 'a' to get "aa", which is
# equal to goal.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, goal.length <= 2 * 10^4
# s and goal consist of lowercase letters.
# 
# 
#

# @lc code=start
class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        c_s = Counter(s)
        c_goal = Counter(goal)
        if c_s != c_goal: return False
        cnt = 0
        for i in range(len(s)):
            if s[i] != goal[i]: cnt += 1
        return cnt == 2 or (not cnt and any(x > 1 for x in c_s.values()))
# @lc code=end

