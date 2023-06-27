#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# https://leetcode.com/problems/plus-one/description/
#
# algorithms
# Easy (43.28%)
# Likes:    5345
# Dislikes: 4469
# Total Accepted:    1.4M
# Total Submissions: 3.2M
# Testcase Example:  '[1,2,3]'
#
# You are given a large integer represented as an integer array digits, where
# each digits[i] is the i^th digit of the integer. The digits are ordered from
# most significant to least significant in left-to-right order. The large
# integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of
# digits.
#
#
# Example 1:
#
#
# Input: digits = [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Incrementing by one gives 123 + 1 = 124.
# Thus, the result should be [1,2,4].
#
#
# Example 2:
#
#
# Input: digits = [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.
# Incrementing by one gives 4321 + 1 = 4322.
# Thus, the result should be [4,3,2,2].
#
#
# Example 3:
#
#
# Input: digits = [9]
# Output: [1,0]
# Explanation: The array represents the integer 9.
# Incrementing by one gives 9 + 1 = 10.
# Thus, the result should be [1,0].
#
#
#
# Constraints:
#
#
# 1 <= digits.length <= 100
# 0 <= digits[i] <= 9
# digits does not contain any leading 0's.
#
#
#

# @lc code=start
from typing import List

# TC: O(n)  SC: O(1)
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        return [1]+digits
# @lc code=end
