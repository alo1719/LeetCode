#
# @lc app=leetcode.cn id=785 lang=python3
#
# [785] Is Graph Bipartite?
#
# https://leetcode.cn/problems/is-graph-bipartite/description/
#
# algorithms
# Medium (54.72%)
# Likes:    480
# Dislikes: 0
# Total Accepted:    81.6K
# Total Submissions: 148.8K
# Testcase Example:  '[[1,2,3],[0,2],[0,1,3],[0,2]]'
#
# There is an undirected graph with n nodes, where each node is numbered
# between 0 and n - 1. You are given a 2D array graph, where graph[u] is an
# array of nodes that node u is adjacent to. More formally, for each v in
# graph[u], there is an undirected edge between node u and node v. The graph
# has the following properties:
# 
# 
# There are no self-edges (graph[u] does not contain u).
# There are no parallel edges (graph[u] does not contain duplicate values).
# If v is in graph[u], then u is in graph[v] (the graph is undirected).
# The graph may not be connected, meaning there may be two nodes u and v such
# that there is no path between them.
# 
# 
# A graph is bipartite if the nodes can be partitioned into two independent
# sets A and B such that every edge in the graph connects a node in set A and a
# node in set B.
# 
# Return true if and only if it is bipartite.
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: There is no way to partition the nodes into two independent sets
# such that every edge connects a node in one and a node in the other.
# 
# Example 2:
# 
# 
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.
# 
# 
# Constraints:
# 
# 
# graph.length == n
# 1 <= n <= 100
# 0 <= graph[u].length < n
# 0 <= graph[u][i] <= n - 1
# graph[u] does not contain u.
# All the values of graph[u] are unique.
# If graph[u] contains v, then graph[v] contains u.
# 
# 
#

# @lc code=start
class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]  # array DSU

    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])  # path compression, O(alpha(n)) average, O(logn) worst
        return self.root[x]
    
    def union(self, a, b, v=1):  # v for weighted DSU
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b

# TC: O(v+e)  SC: O(v)
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        dsu = DSU(n)
        for node in range(n):
            for to_node in graph[node]:
                if dsu.find(node) == dsu.find(to_node): return False
                else: dsu.union(graph[node][0], to_node)
        return True
# @lc code=end

