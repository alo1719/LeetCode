#
# @lc app=leetcode.cn id=261 lang=python3
#
# [261] Graph Valid Tree
#
# https://leetcode.cn/problems/graph-valid-tree/description/
#
# algorithms
# Medium (51.02%)
# Likes:    206
# Dislikes: 0
# Total Accepted:    16.9K
# Total Submissions: 33.2K
# Testcase Example:  '5\n[[0,1],[0,2],[0,3],[1,4]]'
#
# You have a graph of n nodes labeled from 0 to n - 1. You are given an integer
# n and a list of edges where edges[i] = [ai, bi] indicates that there is an
# undirected edge between nodes ai and bi in the graph.
# 
# Return true if the edges of the given graph make up a valid tree, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: n = 5, edges = [[0,1],[0,2],[0,3],[1,4]]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: n = 5, edges = [[0,1],[1,2],[2,3],[1,3],[1,4]]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 2000
# 0 <= edges.length <= 5000
# edges[i].length == 2
# 0 <= ai, bi < n
# ai != bi
# There are no self-loops or repeated edges.
# 
# 
#

# @lc code=start
from typing import List
from collections import defaultdict, deque


# TC: O(v+e)  SC: O(e)
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        m = len(edges)
        if m != n-1: return False
        e_table = defaultdict(list)
        for edge in edges:
            fst, sec = edge[0], edge[1]
            e_table[fst].append(sec)
            e_table[sec].append(fst)
        dq = deque([0])
        visited = [False] * n
        visited[0] = True
        while dq:
            node = dq.popleft()
            for to_node in e_table[node]:
                if not visited[to_node]: dq.append(to_node)
                visited[to_node] = True
        return all(visited)
# @lc code=end

