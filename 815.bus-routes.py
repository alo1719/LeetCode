#
# @lc app=leetcode.cn id=815 lang=python3
#
# [815] Bus Routes
#
# https://leetcode.cn/problems/bus-routes/description/
#
# algorithms
# Hard (44.39%)
# Likes:    348
# Dislikes: 0
# Total Accepted:    38K
# Total Submissions: 85.8K
# Testcase Example:  '[[1,2,7],[3,6,7]]\n1\n6'
#
# You are given an array routes representing bus routes where routes[i] is a
# bus route that the i^th bus repeats forever.
# 
# 
# For example, if routes[0] = [1, 5, 7], this means that the 0^th bus travels
# in the sequence 1 -> 5 -> 7 -> 1 -> 5 -> 7 -> 1 -> ... forever.
# 
# 
# You will start at the bus stop source (You are not on any bus initially), and
# you want to go to the bus stop target. You can travel between bus stops by
# buses only.
# 
# Return the least number of buses you must take to travel from source to
# target. Return -1 if it is not possible.
# 
# 
# Example 1:
# 
# 
# Input: routes = [[1,2,7],[3,6,7]], source = 1, target = 6
# Output: 2
# Explanation: The best strategy is take the first bus to the bus stop 7, then
# take the second bus to the bus stop 6.
# 
# 
# Example 2:
# 
# 
# Input: routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]], source = 15, target
# = 12
# Output: -1
# 
# 
# 
# Constraints:
# 
# 
# 1 <= routes.length <= 500.
# 1 <= routes[i].length <= 10^5
# All the values of routes[i] are unique.
# sum(routes[i].length) <= 10^5
# 0 <= routes[i][j] < 10^6
# 0 <= source, target < 10^6
# 
# 
#

# @lc code=start
# TC: O(nm)  SC: O(nm)  m: number of stops
class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        if source == target: return 0
        n = len(routes)  # treat each route as a node
        stop2route = defaultdict(list)
        for i in range(n):
            routes[i] = set(routes[i])
            for stop in routes[i]:
                stop2route[stop].append(i)
        dq = deque()
        vis = [False]*n  # i-th route is visited
        for i, route in enumerate(routes):
            if source in route:
                dq.append((i, 1))
                vis[i] = True
        while dq:
            i, step = dq.popleft()
            route = routes[i]
            if target in route: return step
            for stop in route:
                for to_route in stop2route[stop]:
                    if not vis[to_route]:
                        vis[to_route] = True
                        dq.append((to_route, step+1))
        return -1
# @lc code=end

