#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Medium (33.07%)
# Likes:    5620
# Dislikes: 1107
# Total Accepted:    658K
# Total Submissions: 2M
# Testcase Example:  '10'
#
# Given an integer n, return the number of prime numbers that are strictly less
# than n.
#
#
# Example 1:
#
#
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
# Example 2:
#
#
# Input: n = 0
# Output: 0
#
#
# Example 3:
#
#
# Input: n = 1
# Output: 0
#
#
#
# Constraints:
#
#
# 0 <= n <= 5 * 10^6
#
#
#

# @lc code=start
from typing import List


class Solution:
    def countPrimes(self, n: int) -> int:
        a: List[bool] = [True] * max(2, n)
        a[0] = a[1] = False
        for i in range(2, n):
            if a[i]:
                for j in range(i * i, n, i):
                    a[j] = False
        return sum(a)

# @lc code=end
