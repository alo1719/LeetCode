#
# @lc app=leetcode.cn id=400 lang=python3
#
# [400] Nth Digit
#
# https://leetcode.cn/problems/nth-digit/description/
#
# algorithms
# Medium (45.66%)
# Likes:    356
# Dislikes: 0
# Total Accepted:    55.1K
# Total Submissions: 120.6K
# Testcase Example:  '3'
#
# Given an integer n, return the n^th digit of the infinite integer sequence
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, ...].
# 
# 
# Example 1:
# 
# 
# Input: n = 3
# Output: 3
# 
# 
# Example 2:
# 
# 
# Input: n = 11
# Output: 0
# Explanation: The 11^th digit of the sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
# 11, ... is a 0, which is part of the number 10.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2^31 - 1
# 
# 
#

# @lc code=start
class Solution:
    def findNthDigit(self, n: int) -> int:
        def calcD(num):
            if num==0: return 0
            ans=0
            n=len(str(num))
            t=int("1"+(n-1)*"0")
            ans+=(num-t+1)*len(str(num))
            ans+=calcD(t-1)
            return ans
        l=1
        r=n
        while l<r:
            m=l+(r-l)//2
            # print(m, calcD(m))
            if (calcD(m)>=n):
                r=m
            else:
                l=m+1
        left=n-calcD(l-1)
        print(int(str(l)[left-1]))
        return int(str(l)[left-1])
# @lc code=end

