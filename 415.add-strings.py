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
# TC: O(max(m,n))  SC: O(max(m,n))
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m, n, carry_out, ans = len(num1), len(num2), 0, []
        if m < n:  # make sure num1 is larger
            num1, num2 = num2, num1
            m, n = n, m
        for i in range(1, m+1):
            digit_1 = num1[-i]
            digit_2 = num2[-i] if i <= n else 0
            carry_out += int(digit_1)+int(digit_2)
            ans.append(str(carry_out%10))
            carry_out //= 10
        if carry_out: ans.append(str(carry_out))
        return ''.join(ans)[::-1]
    
    def subtractStrings(self, num1: str, num2: str) -> str:
        m, n, borrow_in, swapped, ans = len(num1), len(num2), 0, False, []
        if m < n: # make sure num1 is larger
            num1, num2 = num2, num1
            m, n = n, m
            swapped = True
        if m == n:
            for i in range(m):
                if num1[i] < num2[i]:
                    num1, num2 = num2, num1
                    swapped = True
                    break
                elif num1[i] > num2[i]:
                    break
        for i in range(1, m+1):
            digit_1 = num1[-i]
            digit_2 = num2[-i] if i <= n else 0
            tmp = int(digit_1)-int(digit_2)-borrow_in
            borrow_in = 0
            if tmp < 0:
                tmp += 10
                borrow_in = 1
            ans.append(str(tmp))
        if ans[-1] == '0': ans.pop()
        return ''.join(ans)[::-1] if not swapped else '-'+''.join(ans)[::-1]
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
