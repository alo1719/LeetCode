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
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m={}
        l=[]
        r={}
        for i in range(0,len(equations)):
            fst=equations[i][0]
            sec=equations[i][1]
            if fst not in m:
                m[fst]={}
                r[fst]={}
                l.append(fst)
            if sec not in m:
                m[sec]={}
                r[sec]={}
                l.append(sec)
            m[fst][sec]=values[i]
            m[sec][fst]=1/values[i]
            r[fst][sec]=[fst,sec]
            r[sec][fst]=[sec,fst]
        print(m)
        print(l)
        for k in l:
            for i in l:
                for j in l:
                    if j not in m[i] and (k in m[i] and j in m[k]):
                        m[i][j]=m[i][k]*m[k][j]
                        r[i][j]=r[i][k]+r[k][j]
        print(m)
        ans=[]
        ans2=[]
        for q in queries:
            fst=q[0]
            sec=q[1]
            if fst in m and sec in m and sec in m[fst]:
                ans.append(m[fst][sec])
                ans2.append(r[fst][sec])
            else:
                ans.append(-1)
                ans2.append("Not Possible")
        print(ans2)
        return ans
# @lc code=end
