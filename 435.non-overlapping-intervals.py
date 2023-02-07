#
# @lc app=leetcode.cn id=435 lang=python3
#
# [435] Non-overlapping Intervals
#
# https://leetcode.cn/problems/non-overlapping-intervals/description/
#
# algorithms
# Medium (51.15%)
# Likes:    877
# Dislikes: 0
# Total Accepted:    195.9K
# Total Submissions: 382.9K
# Testcase Example:  '[[1,2],[2,3],[3,4],[1,3]]'
#
# Given an array of intervals intervals where intervals[i] = [starti, endi],
# return the minimum number of intervals you need to remove to make the rest of
# the intervals non-overlapping.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of the intervals are
# non-overlapping.
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of the intervals
# non-overlapping.
# 
# 
# Example 3:
# 
# 
# Input: intervals = [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're
# already non-overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^5
# intervals[i].length == 2
# -5 * 10^4 <= starti < endi <= 5 * 10^4
# 
# 
#

# @lc code=start
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        sorted_intervals = sorted(intervals, key=lambda x:x[1])
        ans, n, last = 0, len(intervals), sorted_intervals[0][1]
        for i in range(1, n):
            if sorted_intervals[i][0] < last:
                ans += 1
            else:
                last = sorted_intervals[i][1]
        return ans
# @lc code=end

