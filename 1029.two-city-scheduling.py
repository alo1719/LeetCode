#
# @lc app=leetcode.cn id=1029 lang=python3
#
# [1029] Two City Scheduling
#
# https://leetcode.cn/problems/two-city-scheduling/description/
#
# algorithms
# Medium (68.85%)
# Likes:    304
# Dislikes: 0
# Total Accepted:    25.4K
# Total Submissions: 36.9K
# Testcase Example:  '[[10,20],[30,200],[400,50],[30,20]]'
#
# A company is planning to interview 2n people. Given the array costs where
# costs[i] = [aCosti, bCosti], the cost of flying the i^th person to city a is
# aCosti, and the cost of flying the i^th person to city b is bCosti.
# 
# Return the minimum cost to fly every person to a city such that exactly n
# people arrive in each city.
# 
# 
# Example 1:
# 
# 
# Input: costs = [[10,20],[30,200],[400,50],[30,20]]
# Output: 110
# Explanation: 
# The first person goes to city A for a cost of 10.
# The second person goes to city A for a cost of 30.
# The third person goes to city B for a cost of 50.
# The fourth person goes to city B for a cost of 20.
# 
# The total minimum cost is 10 + 30 + 50 + 20 = 110 to have half the people
# interviewing in each city.
# 
# 
# Example 2:
# 
# 
# Input: costs = [[259,770],[448,54],[926,667],[184,139],[840,118],[577,469]]
# Output: 1859
# 
# 
# Example 3:
# 
# 
# Input: costs =
# [[515,563],[451,713],[537,709],[343,819],[855,779],[457,60],[650,359],[631,42]]
# Output: 3086
# 
# 
# 
# Constraints:
# 
# 
# 2 * n == costs.length
# 2 <= costs.length <= 100
# costs.length is even.
# 1 <= aCosti, bCosti <= 1000
# 
# 
#

# @lc code=start
# TC: O(nlogn)  SC: O(1)
class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key=lambda x:x[0]-x[1], reverse=True)  # how much can save if to b
        ans = 0
        n = len(costs)
        for i in range(n):
            if i < n//2: ans += costs[i][1]
            else: ans += costs[i][0]
        return ans
# @lc code=end

