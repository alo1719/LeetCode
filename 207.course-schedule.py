#
# @lc app=leetcode id=207 lang=python3
#
# [207] Course Schedule
#
# https://leetcode.com/problems/course-schedule/description/
#
# algorithms
# Medium (45.44%)
# Likes:    13712
# Dislikes: 553
# Total Accepted:    1.2M
# Total Submissions: 2.6M
# Testcase Example:  '2\n[[1,0]]'
#
# There are a total of numCourses courses you have to take, labeled from 0 to
# numCourses - 1. You are given an array prerequisites where prerequisites[i] =
# [ai, bi] indicates that you must take course bi first if you want to take
# course ai.
# 
# 
# For example, the pair [0, 1], indicates that to take course 0 you have to
# first take course 1.
# 
# 
# Return true if you can finish all courses. Otherwise, return false.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: true
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0. So it is possible.
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
# Output: false
# Explanation: There are a total of 2 courses to take. 
# To take course 1 you should have finished course 0, and to take course 0 you
# should also have finished course 1. So it is impossible.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= 5000
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# All the pairs prerequisites[i] are unique.
# 
# 
#

# @lc code=start
#  TC: O(v+e)  SC: O(v+e)
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        n, ps = numCourses, prerequisites
        in_degree = [0]*n
        g = defaultdict(list)
        for i, p in enumerate(ps):
            in_degree[p[0]] += 1
            g[p[1]].append(p[0])
        dq = deque([i for i in range(n) if in_degree[i] == 0])
        while dq:
            lenn = len(dq)
            for _ in range(lenn):
                node = dq.popleft()
                if not (n := n-1): return True
                for to_node in g[node]:
                    in_degree[to_node] -= 1
                    if in_degree[to_node] == 0:
                        dq.append(to_node)
        return False
# @lc code=end

