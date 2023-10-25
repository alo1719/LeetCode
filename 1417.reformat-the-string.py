#
# @lc app=leetcode.cn id=1417 lang=python3
#
# [1417] Reformat The String
#
# https://leetcode.cn/problems/reformat-the-string/description/
#
# algorithms
# Easy (55.38%)
# Likes:    92
# Dislikes: 0
# Total Accepted:    46K
# Total Submissions: 83.1K
# Testcase Example:  '"a0b1c2"'
#
# You are given an alphanumeric string s. (Alphanumeric string is a string
# consisting of lowercase English letters and digits).
# 
# You have to find a permutation of the string where no letter is followed by
# another letter and no digit is followed by another digit. That is, no two
# adjacent characters have the same type.
# 
# Return the reformatted string or return an empty string if it is impossible
# to reformat the string.
# 
# 
# Example 1:
# 
# 
# Input: s = "a0b1c2"
# Output: "0a1b2c"
# Explanation: No two adjacent characters have the same type in "0a1b2c".
# "a0b1c2", "0a1b2c", "0c2a1b" are also valid permutations.
# 
# 
# Example 2:
# 
# 
# Input: s = "leetcode"
# Output: ""
# Explanation: "leetcode" has only characters so we cannot separate them by
# digits.
# 
# 
# Example 3:
# 
# 
# Input: s = "1229857369"
# Output: ""
# Explanation: "1229857369" has only digits so we cannot separate them by
# characters.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 500
# s consists of only lowercase English letters and/or digits.
# 
# 
#

# @lc code=start
class Solution:
    def reformat(self, s: str) -> str:
        num_count = []
        char_count = []
        for i, ch in enumerate(s):
            if ord('0') <= ord(ch) <= ord('9'):
                num_count.append(i)
            else:
                char_count.append(i)
        if abs(len(num_count) - len(char_count)) > 1: return ""
        ans = ""
        if len(num_count) > len(char_count):
            for i in range(min(len(num_count), len(char_count))):
                ans += s[num_count[i]] + s[char_count[i]]
            ans += s[num_count[-1]]
        elif len(num_count) < len(char_count):
            for i in range(min(len(num_count), len(char_count))):
                ans += s[char_count[i]] + s[num_count[i]]
            ans += s[char_count[-1]]
        else:
            for i in range(min(len(num_count), len(char_count))):
                ans += s[char_count[i]] + s[num_count[i]]
        return ans
# @lc code=end

