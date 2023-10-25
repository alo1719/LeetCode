#
# @lc app=leetcode.cn id=802 lang=python3
#
# [802] Find Eventual Safe States
#
# https://leetcode.cn/problems/find-eventual-safe-states/description/
#
# algorithms
# Medium (59.16%)
# Likes:    412
# Dislikes: 0
# Total Accepted:    46.4K
# Total Submissions: 78.5K
# Testcase Example:  '[[1,2],[2,3],[5],[0],[5],[],[]]'
#
# There is a directed graph of n nodes with each node labeled from 0 to n - 1.
# The graph is represented by a 0-indexed 2D integer array graph where graph[i]
# is an integer array of nodes adjacent to node i, meaning there is an edge
# from node i to each node in graph[i].
# 
# A node is a terminal node if there are no outgoing edges. A node is a safe
# node if every possible path starting from that node leads to a terminal node
# (or another safe node).
# 
# Return an array containing all the safe nodes of the graph. The answer should
# be sorted in ascending order.
# 
# 
# Example 1:
# 
# 
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
# Nodes 5 and 6 are terminal nodes as there are no outgoing edges from either
# of them.
# Every path starting at nodes 2, 4, 5, and 6 all lead to either node 5 or 6.
# 
# Example 2:
# 
# 
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]
# Explanation:
# Only node 4 is a terminal node, and every path starting at node 4 leads to
# node 4.
# 
# 
# 
# Constraints:
# 
# 
# n == graph.length
# 1 <= n <= 10^4
# 0 <= graph[i].length <= n
# 0 <= graph[i][j] <= n - 1
# graph[i] is sorted in a strictly increasing order.
# The graph may contain self-loops.
# The number of edges in the graph will be in the range [1, 4 * 10^4].
# 
# 
#

# @lc code=start
class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # find terminal
        n = len(graph)
        to_deg = [0]*n
        edge_from = defaultdict(list)
        for i, edges in enumerate(graph):
            to_deg[i] = len(edges)
            for to_node in edges:
                edge_from[to_node].append(i)
        dq = deque([x for x in range(n) if not to_deg[x]])
        ans = set()
        while dq:
            node = dq.popleft()
            ans.add(node)
            for from_node in edge_from[node]:
                to_deg[from_node] -= 1
                if to_deg[from_node] <= 0:
                    dq.append(from_node)
        return [x for x in range(n) if x in ans]
# @lc code=end

