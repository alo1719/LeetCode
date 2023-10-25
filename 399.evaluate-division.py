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
# '[2.0,3.0]\n' +
# '[["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]'
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
# No contradiction, meaning all paths from a -> b have the same value, only need to consider one path
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # 1. floyd considering have multiple queries
        # TC: O(v^3)  SC: O(e)
        g = defaultdict(lambda: defaultdict(float))
        for i, e in enumerate(equations):
            fst, sec = e[0], e[1]
            g[fst][sec] = values[i]
            g[sec][fst] = 1/values[i]
        nodes = g.keys()
        for k in nodes:
            for i in nodes:
                for j in nodes:
                    g[i][j] = max(g[i][j], g[i][k]*g[k][j])
        ans = []
        for q in queries:
            fst, sec = q[0], q[1]
            ans.append(g[fst][sec] if g[fst][sec] != 0 else -1)
        return ans
        # 2. bfs, suitable for only one query
        # TC: O(q(v+e))  SC: O(e)
        g = defaultdict(lambda: defaultdict(float))
        for i, e in enumerate(equations):
            fst, sec = e[0], e[1]
            g[fst][sec] = values[i]
            g[sec][fst] = 1/values[i]
        ans = []
        for q in queries:
            fr, to = q[0], q[1]
            dq = deque()
            if fr in g: dq.append((fr, 1))
            visited = set()
            while dq:
                node = dq.popleft()
                if node[0] == to:
                    ans.append(node[1])
                    break
                visited.add(node[0])
                for to_node in g[node[0]]:
                    if not to_node in visited:
                        dq.append((to_node, node[1]*g[node[0]][to_node]))
            else: ans.append(-1)
        return ans
        # 3. Disjoint Set Union with Weight, overkill
        # TC: O(e)  SC: O(v)
        dsuw = DSUW()
        for (a, b), v in zip(equations, values):
            dsuw.add(a)
            dsuw.add(b)
            dsuw.merge(a, b, v)
        ans = []
        for (a, b) in queries:
            if a in dsuw.root and b in dsuw.root and dsuw.find(a) == dsuw.find(b):
                ans.append(dsuw.weight[a]/dsuw.weight[b])
            else:
                ans.append(-1)
        return ans

class DSUW:
    def __init__(self):
        self.root = defaultdict(int)
        self.weight = defaultdict(float)
    
    def find(self, x):
        if self.root[x] == x: return x
        original_root = self.root[x]
        self.root[x] = self.find(self.root[x])  # path compression
        self.weight[x] *= self.weight[original_root]
        return self.root[x]
    
    def merge(self, a, b, v):
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b
        self.weight[root_a] = v/self.weight[a]*self.weight[b]

    def add(self, x):
        if x not in self.root:
            self.root[x] = x
            self.weight[x] = 1

class DSU:
    def __init__(self, n):
        self.root = [i for i in range(n)]
    
    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])  # path compression
        return self.root[x]
    
    def merge(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        self.root[root_a] = root_b
# @lc code=end
