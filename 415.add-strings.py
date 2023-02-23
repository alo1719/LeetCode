#
# @lc app=leetcode.cn id=415 lang=python3
#
# [415] Add Strings
#
# https://leetcode.cn/problems/add-strings/description/
#
# algorithms
# Easy (54.98%)
# Likes:    671
# Dislikes: 0
# Total Accepted:    249K
# Total Submissions: 452.9K
# Testcase Example:  '"11"\n"123"'
#
# Given two non-negative integers, num1 and num2 represented as string, return
# the sum of num1 and num2 as a string.
# 
# You must solve the problem without using any built-in library for handling
# large integers (such as BigInteger). You must also not convert the inputs to
# integers directly.
# 
# 
# Example 1:
# 
# 
# Input: num1 = "11", num2 = "123"
# Output: "134"
# 
# 
# Example 2:
# 
# 
# Input: num1 = "456", num2 = "77"
# Output: "533"
# 
# 
# Example 3:
# 
# 
# Input: num1 = "0", num2 = "0"
# Output: "0"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= num1.length, num2.length <= 10^4
# num1 and num2 consist of only digits.
# num1 and num2 don't have any leading zeros except for the zero itself.
# 
# 
#

# @lc code=start
# Snowflake VOE
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        n, m, carry_out = len(num1), len(num2), 0
        if n < m: # make sure num1 is larger
            num1, num2 = num2, num1
            n, m = m, n
        ans = ""
        for i in range(1, n+1):
            digit_1 = num1[-i]
            if i <= m:
                digit_2 = num2[-i]
            else:
                digit_2 = 0
            ans = str((int(digit_1) + int(digit_2) + carry_out) % 10) + ans
            carry_out = (int(digit_1) + int(digit_2) + carry_out) // 10
        if carry_out != 0:
            ans = str(carry_out) + ans
        return ans
    
    def subtractStrings(self, num1: str, num2: str) -> str:
        n, m, borrow_in,swapped = len(num1), len(num2), 0, False
        if n < m: # make sure num1 is larger
            num1, num2 = num2, num1
            n, m = m, n
            swapped = True
        if n == m:
            for i in range(n):
                if num1[i] < num2[i]:
                    num1, num2 = num2, num1
                    swapped = True
                    break
                elif num1[i] > num2[i]:
                    break
        ans = ""
        for i in range(1, n+1):
            digit_1 = num1[-i]
            if i <= m:
                digit_2 = num2[-i]
            else:
                digit_2 = 0
            tmp_res = int(digit_1) - int(digit_2) - borrow_in
            borrow_in = 0
            if tmp_res < 0:
                tmp_res += 10
                borrow_in = 1
            ans = str(tmp_res) + ans
        if ans[0] == '0':
            ans = ans[1:]
        return ans if not swapped else '-' + ans
# @lc code=end

print(Solution().subtractStrings("11", "123"))
print(Solution().subtractStrings("15", "16"))
print(Solution().subtractStrings("16", "16"))
print(Solution().subtractStrings("16", "15"))
print(Solution().subtractStrings("9", "1233"))
print(Solution().subtractStrings("1233", "9"))
print(Solution().subtractStrings("1231233", "934231"))
print(Solution().subtractStrings("934231", "1231233"))
print(Solution().subtractStrings("93423131234412", "7451123971233"))
