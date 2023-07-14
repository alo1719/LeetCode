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

# TC: O(nloglogn) (hard to prove)  SC: O(n)
class Solution:
    def countPrimes(self, n: int) -> int:
        prime = [True]*(n)
        for i in range(2, n):
            if prime[i]:
                j = i*i
                while j < n:
                    prime[j] = False
                    j += i
        return prime[2:].count(True)

# @lc code=end
