#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] Course Schedule II
#
# https://leetcode.cn/problems/course-schedule-ii/description/
#
# algorithms
# Medium (56.34%)
# Likes:    723
# Dislikes: 0
# Total Accepted:    157.1K
# Total Submissions: 278.9K
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
# Return the ordering of courses you should take to finish all courses. If
# there are many valid answers, return any of them. If it is impossible to
# finish all courses, return an empty array.
# 
# 
# Example 1:
# 
# 
# Input: numCourses = 2, prerequisites = [[1,0]]
# Output: [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you
# should have finished course 0. So the correct course order is [0,1].
# 
# 
# Example 2:
# 
# 
# Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
# Output: [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you
# should have finished both courses 1 and 2. Both courses 1 and 2 should be
# taken after you finished course 0.
# So one correct course order is [0,1,2,3]. Another correct ordering is
# [0,2,1,3].
# 
# 
# Example 3:
# 
# 
# Input: numCourses = 1, prerequisites = []
# Output: [0]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= numCourses <= 2000
# 0 <= prerequisites.length <= numCourses * (numCourses - 1)
# prerequisites[i].length == 2
# 0 <= ai, bi < numCourses
# ai != bi
# All the pairs [ai, bi] are distinct.
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # 1. Build graph
        g = [[] for _ in range(numCourses)]
        for course, pre in prerequisites:
            g[course].append(pre)
        # print(g)
        v = [False] * numCourses
        r = []
        # 2. DFS
        def dfs(c):
            if v[c]:
                return
            v[c] = True
            r.append(c)
            for course in range(numCourses):
                if v[course]: continue
                course_ok = True
                for pre in g[course]:
                    if not v[pre]:
                        course_ok = False
                        break
                if course_ok:
                    dfs(course)
        
        for c in range(numCourses):
            if not g[c]:
                dfs(c)
        
        for vv in v:
            if not vv:
                return []
        return r



# @lc code=end

