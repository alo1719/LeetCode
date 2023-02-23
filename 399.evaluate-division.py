#
# @lc app=leetcode.cn id=399 lang=python3
#
# [399] Evaluate Division
#
# https://leetcode.cn/problems/evaluate-division/description/
#
# algorithms
# Medium (59.42%)
# Likes:    878
# Dislikes: 0
# Total Accepted:    69.9K
# Total Submissions: 117.6K
# Testcase Example:  '[["a","b"],["b","c"]]\n' +
  '[2.0,3.0]\n' +
  '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
#
# You are given an array of variable pairs equations and an array of real
# numbers values, where equations[i] = [Ai, Bi] and values[i] represent the
# equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a
# single variable.
# 
# You are also given some queries, where queries[j] = [Cj, Dj] represents the
# j^th query where you must find the answer for Cj / Dj = ?.
# 
# Return the answers to all queries. If a single answer cannot be determined,
# return -1.0.
# 
# Note: The input is always valid. You may assume that evaluating the queries
# will not result in division by zero and that there is no contradiction.
# 
# 
# Example 1:
# 
# 
# Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries =
# [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
# Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
# Explanation: 
# Given: a / b = 2.0, b / c = 3.0
# queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
# return: [6.0, 0.5, -1.0, 1.0, -1.0 ]
# 
# 
# Example 2:
# 
# 
# Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0],
# queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
# Output: [3.75000,0.40000,5.00000,0.20000]
# 
# 
# Example 3:
# 
# 
# Input: equations = [["a","b"]], values = [0.5], queries =
# [["a","b"],["b","a"],["a","c"],["x","y"]]
# Output: [0.50000,2.00000,-1.00000,-1.00000]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= equations.length <= 20
# equations[i].length == 2
# 1 <= Ai.length, Bi.length <= 5
# values.length == equations.length
# 0.0 < values[i] <= 20.0
# 1 <= queries.length <= 20
# queries[i].length == 2
# 1 <= Cj.length, Dj.length <= 5
# Ai, Bi, Cj, Dj consist of lower case English letters and digits.
# 
# 
#

# @lc code=start
# Snowflake VOE
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. queries much, floyd
        # graph = defaultdict(lambda: defaultdict(lambda: 0))
        # for i, e in enumerate(equations):
        #     fst, sec = e[0], e[1]
        #     graph[fst][sec] = values[i]
        #     graph[sec][fst] = 1/values[i]
        # # floyd
        # nodes = graph.keys()
        # print(nodes)
        # for k in nodes:
        #     for i in nodes:
        #         for j in nodes:
        #             graph[i][j] = max(graph[i][j], graph[i][k]*graph[k][j])
        # print(graph)
        # ans = []
        # for q in queries:
        #     fst, sec = q[0], q[1]
        #     ans.append(graph[fst][sec] if graph[fst][sec] != 0 else -1)
        # return ans
        # 2. queris less, bfs/dijkstra (bfs is easier to impl)
        # graph = defaultdict(lambda: defaultdict(lambda: 0))
        # for i, e in enumerate(equations):
        #     fst, sec = e[0], e[1]
        #     graph[fst][sec] = values[i]
        #     graph[sec][fst] = 1/values[i]
        # ans = []
        # for q in queries:
        #     fr, to = q[0], q[1]
        #     dq = deque()
        #     if fr in graph.keys():
        #         dq.append((fr, 1))
        #     visited = set()
        #     ans_one_time = -1
        #     while dq:
        #         element = dq.popleft()
        #         if element[0] == to: ans_one_time = max(ans_one_time, element[1])
        #         visited.add(element[0])
        #         for node_to in graph[element[0]]:
        #             if not node_to in visited:
        #                 dq.append((node_to, element[1]*graph[element[0]][node_to]))
        #     ans.append(ans_one_time)
        # return ans
        # 3. weighted union find set, optimal but tricky to impl
        wufs = WUFS()
        for (a, b), v in zip(equations, values):
            wufs.add(a)
            wufs.add(b)
            wufs.merge(a, b, v)
        ans = []
        print(wufs.root)
        print(wufs.weight)
        for (a, b) in queries:
            if a in wufs.root and b in wufs.root and wufs.find(a) == wufs.find(b):
                ans.append(wufs.weight[a] / wufs.weight[b])
            else:
                ans.append(-1)
        return ans

class WUFS:
    def __init__(self):
        self.root = defaultdict(int)
        self.weight = defaultdict(int)
    
    def find(self, x):
        if self.root[x] == x: return x
        original_root = self.root[x]
        self.root[x] = self.find(self.root[x]) # path compression
        self.weight[x] *= self.weight[original_root]
        return self.root[x]
    
    def merge(self, a, b, v):
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b
        self.weight[root_a] = v / self.weight[a] * self.weight[b]

    def add(self, x):
        if x not in self.root:
            self.root[x] = x
            self.weight[x] = 1

class UFS:
    def __init__(self, n):
        self.root = [i for i in range(n)]
    
    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x]) # path compression
        return self.root[x]
    
    def merge(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b
# @lc code=end
