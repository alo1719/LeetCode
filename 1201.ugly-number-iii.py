#
# @lc app=leetcode.cn id=1201 lang=python3
#
# [1201] Ugly Number III
#
# https://leetcode.cn/problems/ugly-number-iii/description/
#
# algorithms
# Medium (26.98%)
# Likes:    119
# Dislikes: 0
# Total Accepted:    9.6K
# Total Submissions: 35.4K
# Testcase Example:  '3\n2\n3\n5'
#
# An ugly number is a positive integer that is divisible by a, b, or c.
#
# Given four integers n, a, b, and c, return the n^th ugly number.
#
#
# Example 1:
#
#
# Input: n = 3, a = 2, b = 3, c = 5
# Output: 4
# Explanation: The ugly numbers are 2, 3, 4, 5, 6, 8, 9, 10... The 3^rd is 4.
#
#
# Example 2:
#
#
# Input: n = 4, a = 2, b = 3, c = 4
# Output: 6
# Explanation: The ugly numbers are 2, 3, 4, 6, 8, 9, 10, 12... The 4^th is
# 6.
#
#
# Example 3:
#
#
# Input: n = 5, a = 2, b = 11, c = 13
# Output: 10
# Explanation: The ugly numbers are 2, 4, 6, 8, 10, 11, 12, 13... The 5^th is
# 10.
#
#
#
# Constraints:
#
#
# 1 <= n, a, b, c <= 10^9
# 1 <= a * b * c <= 10^18
# It is guaranteed that the result will be in range [1, 2 * 10^9].
#
#
#

# @lc code=start
class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        def gcd(x, y):
            if y == 0:
                return x
            return gcd(y, x%y)

        def lcm(x, y):
            return x*y//gcd(x, y)

        def count(x):
            return x//a+x//b+x//c-x//lcm(a, b)-x//lcm(b, c)-x//lcm(a, c)+x//lcm(a, lcm(b, c))

        l, r = 1, 2*10**9
        while l < r:
            mid = (l+r)//2
            if count(mid) < n:
                l = mid+1
            else:
                r = mid
        return l
# @lc code=end
