#
# @lc app=leetcode id=771 lang=python3
#
# [771] Jewels and Stones
#
# https://leetcode.com/problems/jewels-and-stones/description/
#
# algorithms
# Easy (88.26%)
# Likes:    4678
# Dislikes: 553
# Total Accepted:    901.8K
# Total Submissions: 1M
# Testcase Example:  '"aA"\n"aAAbbbb"'
#
# You're given strings jewels representing the types of stones that are jewels,
# and stones representing the stones you have. Each character in stones is a
# type of stone you have. You want to know how many of the stones you have are
# also jewels.
# 
# Letters are case sensitive, so "a" is considered a different type of stone
# from "A".
# 
# 
# Example 1:
# Input: jewels = "aA", stones = "aAAbbbb"
# Output: 3
# Example 2:
# Input: jewels = "z", stones = "ZZ"
# Output: 0
# 
# 
# Constraints:
# 
# 
# 1 <= jewels.length, stones.length <= 50
# jewels and stones consist of only English letters.
# All the characters of jewels are unique.
# 
# 
#

# @lc code=start
# TC: O(n+m)  SC: O(n)
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        c = Counter(stones)
        ans = 0
        for j in jewels:
            ans += c[j]
        return ans
# @lc code=end

