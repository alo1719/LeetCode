#
# @lc app=leetcode.cn id=2246 lang=python3
#
# [2246] Longest Path With Different Adjacent Characters
#
# https://leetcode.cn/problems/longest-path-with-different-adjacent-characters/description/
#
# algorithms
# Hard (47.10%)
# Likes:    58
# Dislikes: 0
# Total Accepted:    6.1K
# Total Submissions: 13K
# Testcase Example:  '[-1,0,0,1,1,2]\n"abacbe"'
#
# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
# represented by a 0-indexed array parent of size n, where parent[i] is the
# parent of node i. Since node 0 is the root, parent[0] == -1.
# 
# You are also given a string s of length n, where s[i] is the character
# assigned to node i.
# 
# Return the length of the longest path in the tree such that no pair of
# adjacent nodes on the path have the same character assigned to them.
# 
# 
# Example 1:
# 
# 
# Input: parent = [-1,0,0,1,1,2], s = "abacbe"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters in the tree is the path: 0 -> 1 -> 3. The length of this path is
# 3, so 3 is returned.
# It can be proven that there is no longer path that satisfies the
# conditions. 
# 
# 
# Example 2:
# 
# 
# Input: parent = [-1,0,0,0], s = "aabc"
# Output: 3
# Explanation: The longest path where each two adjacent nodes have different
# characters is the path: 2 -> 0 -> 3. The length of this path is 3, so 3 is
# returned.
# 
# 
# 
# Constraints:
# 
# 
# n == parent.length == s.length
# 1 <= n <= 10^5
# 0 <= parent[i] <= n - 1 for all i >= 1
# parent[0] == -1
# parent represents a valid tree.
# s consists of only lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        def f(x):
            nonlocal ans
            x_len = 0
            for y in g[x]:
                y_len = f(y)+1
                if s[y] != s[x]:
                    ans = max(ans, x_len+y_len)
                    x_len = max(x_len, y_len)
            return x_len
        n = len(parent)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            g[parent[i]].append(i)  # parent not in g
        ans = 0
        f(0)
        return ans+1
# @lc code=end

