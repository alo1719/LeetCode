#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] Merge Intervals
#
# https://leetcode.cn/problems/merge-intervals/description/
#
# algorithms
# Medium (49.25%)
# Likes:    1770
# Dislikes: 0
# Total Accepted:    573.5K
# Total Submissions: 1.2M
# Testcase Example:  '[[1,3],[2,6],[8,10],[15,18]]'
#
# Given an array of intervals where intervals[i] = [starti, endi], merge all
# overlapping intervals, and return an array of the non-overlapping intervals
# that cover all the intervals in the input.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlap, merge them into
# [1,6].
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^4
# 
# 
#

# @lc code=start
# TC: O(nlogn)  SC: O(n)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        ans = []
        for interval in intervals:
            if not ans or interval[0] > ans[-1][-1]:
                ans.append(interval)
            else:
                ans[-1][-1] = max(ans[-1][-1], interval[-1])
        return ans
# @lc code=end
