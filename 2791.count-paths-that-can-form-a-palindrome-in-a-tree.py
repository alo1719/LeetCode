#
# @lc app=leetcode id=2791 lang=python3
#
# [2791] Count Paths That Can Form a Palindrome in a Tree
#
# https://leetcode.com/problems/count-paths-that-can-form-a-palindrome-in-a-tree/description/
#
# algorithms
# Hard (41.61%)
# Likes:    191
# Dislikes: 3
# Total Accepted:    2.4K
# Total Submissions: 5.3K
# Testcase Example:  '[-1,0,0,1,1,2]\n"acaabc"'
#
# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1. The tree is
# represented by a 0-indexed array parent of size n, where parent[i] is the
# parent of node i. Since node 0 is the root, parent[0] == -1.
# 
# You are also given a string s of length n, where s[i] is the character
# assigned to the edge between i and parent[i]. s[0] can be ignored.
# 
# Return the number of pairs of nodes (u, v) such that u < v and the characters
# assigned to edges on the path from u to v can be rearranged to form a
# palindrome.
# 
# A string is a palindrome when it reads the same backwards as forwards.
# 
# 
# Example 1:
# 
# 
# 
# 
# Input: parent = [-1,0,0,1,1,2], s = "acaabc"
# Output: 8
# Explanation: The valid pairs are:
# - All the pairs (0,1), (0,2), (1,3), (1,4) and (2,5) result in one character
# which is always a palindrome.
# - The pair (2,3) result in the string "aca" which is a palindrome.
# - The pair (1,5) result in the string "cac" which is a palindrome.
# - The pair (3,5) result in the string "acac" which can be rearranged into the
# palindrome "acca".
# 
# 
# Example 2:
# 
# 
# Input: parent = [-1,0,0,0,0], s = "aaaaa"
# Output: 10
# Explanation: Any pair of nodes (u,v) where u < v is valid.
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
# TC: O(n)  SC: O(n)
class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        # 0->even time, 1->odd times
        # A--LCA--B = A--LCA + LCA--B
        # LCA--A = root--A - root--LCA
        # operator is ^ in this case
        # A--B = A--LCA ^ LCA--B = LCA--A ^ LCA--B = (root--A ^ root--LCA) ^ (root--B ^ root--LCA) = root--A ^ root--B
        # so root-A ^ root-B should be 0, or has 1 bit set
        def dfs(node, xor_sum):
            nonlocal ans
            ans += cnt[xor_sum]  # xor_sum ^ prev_xor_sum = 0
            for i in range(26):
                ans += cnt[xor_sum^(1<<i)]  # xor_sum ^ prev_xor_sum has 1 bit set
            cnt[xor_sum] += 1
            for to_node, weight in g[node]:
                dfs(to_node, xor_sum^weight)
        n = len(s)
        g = [[] for _ in range(n)]
        for i in range(1, n):
            bit = 1<<(ord(s[i])-ord('a'))
            g[parent[i]].append((i, bit))
        ans = 0
        cnt = Counter()
        dfs(0, 0)
        return ans
# @lc code=end

