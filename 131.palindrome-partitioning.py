#
# @lc app=leetcode.cn id=131 lang=python3
#
# [131] Palindrome Partitioning
#
# https://leetcode.cn/problems/palindrome-partitioning/description/
#
# algorithms
# Medium (73.39%)
# Likes:    1583
# Dislikes: 0
# Total Accepted:    309.2K
# Total Submissions: 421.3K
# Testcase Example:  '"aab"'
#
# Given a string s, partition s such that every substring of the partition is a
# palindrome. Return all possible palindrome partitioning of s.
# 
# 
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Example 2:
# Input: s = "a"
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 16
# s contains only lowercase English letters.
# 
# 
#

# @lc code=start
# TC: O(n*2^n)  SC: O(n)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def dfs(i):
            if i == n:
                ans.append(path[:])
                return
            for j in range(i, n):
                sub = s[i:j+1]
                if sub == sub[::-1]:
                    path.append(sub)
                    dfs(j+1)
                    path.pop()
        ans = []
        path = []
        n = len(s)
        dfs(0)
        return ans
# @lc code=end

