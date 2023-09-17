#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
# https://leetcode.cn/problems/letter-combinations-of-a-phone-number/description/
#
# algorithms
# Medium (57.85%)
# Likes:    2195
# Dislikes: 0
# Total Accepted:    603.8K
# Total Submissions: 1M
# Testcase Example:  '"23"'
#
# Given a string containing digits from 2-9 inclusive, return all possible
# letter combinations that the number could represent. Return the answer in any
# order.
# 
# A mapping of digits to letters (just like on the telephone buttons) is given
# below. Note that 1 does not map to any letters.
# 
# 
# Example 1:
# 
# 
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# 
# 
# Example 2:
# 
# 
# Input: digits = ""
# Output: []
# 
# 
# Example 3:
# 
# 
# Input: digits = "2"
# Output: ["a","b","c"]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= digits.length <= 4
# digits[i] is a digit in the range ['2', '9'].
# 
# 
#

# @lc code=start
# TC: O(n*4^n)  SC: O(n)
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # if only need to return the number of combinations, we can use DP
        def dfs(i):
            if i == len(digits):
                ans.append(''.join(path))
                return
            for ch in mapping[int(digits[i])]:
                path.append(ch)
                dfs(i+1)
                path.pop()

        ans = []
        path = []
        mapping = ["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        if not digits: return []
        dfs(0)
        return ans
# @lc code=end

