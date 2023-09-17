#
# @lc app=leetcode.cn id=67 lang=python3
#
# [67] Add Binary
#
# https://leetcode.cn/problems/add-binary/description/
#
# algorithms
# Easy (52.93%)
# Likes:    1073
# Dislikes: 0
# Total Accepted:    336.7K
# Total Submissions: 636.3K
# Testcase Example:  '"11"\n"1"'
#
# Given two binary strings a and b, return their sum as a binary string.
# 
# 
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
# 
# 
# Constraints:
# 
# 
# 1 <= a.length, b.length <= 10^4
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
# TC: O(max(m, n))  SC: O(max(m, n))
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m, n = len(a), len(b)
        ans = []
        carry = 0
        for i in range(1, max(m, n)+1):
            if i <= m and i <= n:
                carry = int(a[-i])+int(b[-i])+carry
                ans.append(str(carry%2))
                carry //= 2
            elif i <= m:
                carry = int(a[-i])+carry
                ans.append(str(carry%2))
                carry //= 2
            else:
                carry = int(b[-i])+carry
                ans.append(str(carry%2))
                carry //= 2
        if carry: ans.append(str(carry))
        return ''.join(ans)[::-1]
# @lc code=end

