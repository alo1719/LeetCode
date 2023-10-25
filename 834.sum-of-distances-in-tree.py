#
# @lc app=leetcode id=834 lang=python3
#
# [834] Sum of Distances in Tree
#
# https://leetcode.com/problems/sum-of-distances-in-tree/description/
#
# algorithms
# Hard (59.12%)
# Likes:    4674
# Dislikes: 106
# Total Accepted:    83.8K
# Total Submissions: 141.7K
# Testcase Example:  '6\n[[0,1],[0,2],[2,3],[2,4],[2,5]]'
#
# There is an undirected connected tree with n nodes labeled from 0 to n - 1
# and n - 1 edges.
# 
# You are given the integer n and the array edges where edges[i] = [ai, bi]
# indicates that there is an edge between nodes ai and bi in the tree.
# 
# Return an array answer of length n where answer[i] is the sum of the
# distances between the i^th node in the tree and all other nodes.
# 
# 
# Example 1:
# 
# 
# Input: n = 6, edges = [[0,1],[0,2],[2,3],[2,4],[2,5]]
# Output: [8,12,6,10,10,10]
# Explanation: The tree is shown above.
# We can see that dist(0,1) + dist(0,2) + dist(0,3) + dist(0,4) + dist(0,5)
# equals 1 + 1 + 2 + 2 + 2 = 8.
# Hence, answer[0] = 8, and so on.
# 
# 
# Example 2:
# 
# 
# Input: n = 1, edges = []
# Output: [0]
# 
# 
# Example 3:
# 
# 
# Input: n = 2, edges = [[1,0]]
# Output: [1,1]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 3 * 10^4
# edges.length == n - 1
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# The given input represents a valid tree.
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, parent, depth):
            ans[0] += depth
            for child in g[node]:
                if child != parent:
                    dfs(child, node, depth+1)
                    size[node] += size[child]
        def reroot(node, parent):
            for child in g[node]:
                if child != parent:
                    ans[child] = ans[node]+n-2*size[child]  # n-size: nodes outside subtree all +1, size: nodes inside subtree all -1
                    reroot(child, node)
        g = defaultdict(list)
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        ans = [0]*n
        size = [1]*n  # size of subtree
        dfs(0, None, 0)  # calc ans[0] & subtree size
        reroot(0, None)  # calc ans[1:] based on ans[0]
        return ans
# @lc code=end

