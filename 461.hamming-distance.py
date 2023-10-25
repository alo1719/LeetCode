#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#
# https://leetcode.com/problems/hamming-distance/description/
#
# algorithms
# Easy (74.75%)
# Likes:    3276
# Dislikes: 202
# Total Accepted:    494K
# Total Submissions: 660.9K
# Testcase Example:  '1\n4'
#
# The Hamming distance between two integers is the number of positions at which
# the corresponding bits are different.
#
# Given two integers x and y, return the Hamming distance between them.
#
#
# Example 1:
#
#
# Input: x = 1, y = 4
# Output: 2
# Explanation:
# 1   (0 0 0 1)
# 4   (0 1 0 0)
# ⁠      ↑   ↑
# The above arrows point to positions where the corresponding bits are
# different.
#
#
# Example 2:
#
#
# Input: x = 3, y = 1
# Output: 1
#
#
#
# Constraints:
#
#
# 0 <= x, y <= 2^31 - 1
#
#
#

# @lc code=start
#
# @lc app=leetcode id=461 lang=python3
#
# [461] Hamming Distance
#

# @lc code=start
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return bin(x^y).count('1')

# @lc code=end


# @lc code=end
