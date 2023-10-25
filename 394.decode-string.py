#
# @lc app=leetcode.cn id=394 lang=python3
#
# [394] Decode String
#
# https://leetcode.cn/problems/decode-string/description/
#
# algorithms
# Medium (56.77%)
# Likes:    1568
# Dislikes: 0
# Total Accepted:    255.8K
# Total Submissions: 450.6K
# Testcase Example:  '"3[a]2[bc]"'
#
# Given an encoded string, return its decoded string.
# 
# The encoding rule is: k[encoded_string], where the encoded_string inside the
# square brackets is being repeated exactly k times. Note that k is guaranteed
# to be a positive integer.
# 
# You may assume that the input string is always valid; there are no extra
# white spaces, square brackets are well-formed, etc. Furthermore, you may
# assume that the original data does not contain any digits and that digits are
# only for those repeat numbers, k. For example, there will not be input like
# 3a or 2[4].
# 
# The test cases are generated so that the length of the output will never
# exceed 10^5.
# 
# 
# Example 1:
# 
# 
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"
# 
# 
# Example 2:
# 
# 
# Input: s = "3[a2[c]]"
# Output: "accaccacc"
# 
# 
# Example 3:
# 
# 
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 30
# s consists of lowercase English letters, digits, and square brackets
# '[]'.
# s is guaranteed to be a valid input.
# All the integers in s are in the range [1, 300].
# 
# 
#

# @lc code=start
# TC: O(S)  SC: O(S)
class Solution:
    def decodeString(self, s: str) -> str:
        stk = []
        for ch in s:
            if ch == ']':
                tmp = []
                while stk[-1] != '[':
                    tmp.append(stk.pop())
                num = []
                stk.pop()
                while stk and ord('0') <= ord(stk[-1]) <= ord('9'):
                    num.append(stk.pop())
                tmp = ''.join(tmp[::-1])
                num = int(''.join(num[::-1]))
                for _ in range(num):
                    for ch2 in tmp: stk.append(ch2)
            else: stk.append(ch)
        return ''.join(stk)
# @lc code=end

