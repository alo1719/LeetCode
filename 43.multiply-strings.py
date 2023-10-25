#
# @lc app=leetcode id=43 lang=python3
#
# [43] Multiply Strings
#
# https://leetcode.com/problems/multiply-strings/description/
#
# algorithms
# Medium (39.49%)
# Likes:    6644
# Dislikes: 3070
# Total Accepted:    705.2K
# Total Submissions: 1.8M
# Testcase Example:  '"2"\n"3"'
#
# Given two non-negative integers num1 and num2 represented as strings, return
# the product of num1 and num2, also represented as a string.
# 
# Note: You must not use any built-in BigInteger library or convert the inputs
# to integer directly.
# 
# 
# Example 1:
# Input: num1 = "2", num2 = "3"
# Output: "6"
# Example 2:
# Input: num1 = "123", num2 = "456"
# Output: "56088"
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 200
# num1 and num2 consist of digits only.
# Both num1 and num2 do not contain any leading zero, except the number 0
# itself.
# 
# 
#

# @lc code=start
# TC: O(mn)  SC: O(m+n)
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0': return '0'
        m, n = len(num1), len(num2)
        ans = [0]*(m+n)
        for i in range(m-1, -1, -1):
            x = int(num1[i])
            for j in range(n-1, -1, -1):
                y = int(num2[j])
                ans[i+j+1] += x*y
        for i in range(m+n-1, 0, -1):
            ans[i-1] += ans[i]//10
            ans[i] %= 10
        if ans[0] == 0:
            return ''.join(str(x) for x in ans[1:])
        return ''.join(str(x) for x in ans)
# @lc code=end

