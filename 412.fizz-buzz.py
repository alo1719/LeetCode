#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# https://leetcode.com/problems/fizz-buzz/description/
#
# algorithms
# Easy (68.35%)
# Likes:    951
# Dislikes: 158
# Total Accepted:    754K
# Total Submissions: 1.1M
# Testcase Example:  '3'
#
# Given an integer n, return a string array answer (1-indexed) where:
#
#
# answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# answer[i] == "Fizz" if i is divisible by 3.
# answer[i] == "Buzz" if i is divisible by 5.
# answer[i] == i (as a string) if none of the above conditions are true.
#
#
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
# Example 3:
# Input: n = 15
# Output:
# ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
#
# Constraints:
#
#
# 1 <= n <= 10^4
#
#
#

# @lc code=start
from typing import List

# TC: O(n)  SC: O(n)
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        ans = []
        for i in range(1, n+1):
            if i%15 == 0: ans.append("FizzBuzz")
            elif i%3 == 0: ans.append("Fizz")
            elif i%5 == 0: ans.append("Buzz")
            else: ans.append(str(i))
        return ans

# @lc code=end
