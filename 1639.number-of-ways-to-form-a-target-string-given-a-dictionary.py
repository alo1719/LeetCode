#
# @lc app=leetcode id=1639 lang=python3
#
# [1639] Number of Ways to Form a Target String Given a Dictionary
#
# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/description/
#
# algorithms
# Hard (53.90%)
# Likes:    1396
# Dislikes: 70
# Total Accepted:    48.6K
# Total Submissions: 90.1K
# Testcase Example:  '["acca","bbbb","caca"]\n"aba"'
#
# You are given a list of strings of the same length words and a string
# target.
# 
# Your task is to form target using the given words under the following
# rules:
# 
# 
# target should be formed from left to right.
# To form the i^th character (0-indexed) of target, you can choose the k^th
# character of the j^th string in words if target[i] = words[j][k].
# Once you use the k^th character of the j^th string of words, you can no
# longer use the x^th character of any string in words where x <= k. In other
# words, all characters to the left of or at index k become unusuable for every
# string.
# Repeat the process until you form the string target.
# 
# 
# Notice that you can use multiple characters from the same string in words
# provided the conditions above are met.
# 
# Return the number of ways to form target from words. Since the answer may be
# too large, return it modulo 10^9 + 7.
# 
# 
# Example 1:
# 
# 
# Input: words = ["acca","bbbb","caca"], target = "aba"
# Output: 6
# Explanation: There are 6 ways to form target.
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("caca")
# "aba" -> index 0 ("acca"), index 1 ("bbbb"), index 3 ("acca")
# "aba" -> index 0 ("acca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("acca")
# "aba" -> index 1 ("caca"), index 2 ("bbbb"), index 3 ("caca")
# 
# 
# Example 2:
# 
# 
# Input: words = ["abba","baab"], target = "bab"
# Output: 4
# Explanation: There are 4 ways to form target.
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 2 ("abba")
# "bab" -> index 0 ("baab"), index 1 ("baab"), index 3 ("baab")
# "bab" -> index 0 ("baab"), index 2 ("baab"), index 3 ("baab")
# "bab" -> index 1 ("abba"), index 2 ("baab"), index 3 ("baab")
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 1000
# 1 <= words[i].length <= 1000
# All strings in words have the same length.
# 1 <= target.length <= 1000
# words[i] and target contain only lowercase English letters.
# 
# 
#

# @lc code=start
import collections
from typing import List

# TC: O(mn)  SC: O(mn), can be optimized to O(n)
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        m, n = len(target), len(words[0])
        word_chars = []
        for i in range(n):
            word_chars.append(collections.Counter(word[i] for word in words))
        
        # dp[i][j] = # of ways to form target[:i] using words[:j]
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(n+1): dp[0][i] = 1
        for i in range(m):
            for j in range(n):
                dp[i+1][j+1] = word_chars[j][target[i]]*dp[i][j]+dp[i+1][j]

        return dp[-1][-1]%(10**9+7)
# @lc code=end
Solution().numWays(["acca","bbbb","caca"], "aba")
