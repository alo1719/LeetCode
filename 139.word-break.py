#
# @lc app=leetcode.cn id=139 lang=python3
#
# [139] Word Break
#
# https://leetcode.cn/problems/word-break/description/
#
# algorithms
# Medium (54.22%)
# Likes:    2219
# Dislikes: 0
# Total Accepted:    463.3K
# Total Submissions: 854.1K
# Testcase Example:  '"leetcode"\n["leet","code"]'
#
# Given a string s and a dictionary of strings wordDict, return true if s can
# be segmented into a space-separated sequence of one or more dictionary
# words.
# 
# Note that the same word in the dictionary may be reused multiple times in the
# segmentation.
# 
# 
# Example 1:
# 
# 
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet
# code".
# 
# 
# Example 2:
# 
# 
# Input: s = "applepenapple", wordDict = ["apple","pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple
# pen apple".
# Note that you are allowed to reuse a dictionary word.
# 
# 
# Example 3:
# 
# 
# Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 300
# 1 <= wordDict.length <= 1000
# 1 <= wordDict[i].length <= 20
# s and wordDict[i] consist of only lowercase English letters.
# All the strings of wordDict are unique.
# 
# 
#

# @lc code=start
# TC: O(n^2)  SC: O(n)
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # f[i]: s[:i] can be segmented
        # f[i] = f[j] and s[j:i] in wordDict
        wordDict = set(wordDict)
        n = len(s)
        f = [True]+[False]*n
        for i in range(1, n+1):
            for j in range(i):
                if f[j] and s[j:i] in wordDict:
                    f[i] = True
                    break
        return f[-1]
# @lc code=end

