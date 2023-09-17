#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] Insert Interval
#
# https://leetcode.cn/problems/insert-interval/description/
#
# algorithms
# Medium (41.95%)
# Likes:    732
# Dislikes: 0
# Total Accepted:    151.1K
# Total Submissions: 360K
# Testcase Example:  '[[1,3],[6,9]]\n[2,5]'
#
# You are given an array of non-overlapping intervals intervals where
# intervals[i] = [starti, endi] represent the start and the end of the i^th
# interval and intervals is sorted in ascending order by starti. You are also
# given an interval newInterval = [start, end] that represents the start and
# end of another interval.
# 
# Insert newInterval into intervals such that intervals is still sorted in
# ascending order by starti and intervals still does not have any overlapping
# intervals (merge overlapping intervals if necessary).
# 
# Return intervals after the insertion.
# 
# 
# Example 1:
# 
# 
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# 
# 
# Example 2:
# 
# 
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with
# [3,5],[6,7],[8,10].
# 
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti <= endi <= 10^5
# intervals is sorted by starti in ascending order.
# newInterval.length == 2
# 0 <= start <= end <= 10^5
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # classificaiton
        # 1. on the right [1,2] [4,8] x>e, append([b, e])
        # 2. on the left [4,8] [9,10], y<b, append([x, y]) and the rest
        # 3. overlap [1,9] [4,8] the others, x = min(x, b), y = max(y, e)
        x, y = newInterval
        ans = []
        for i, (b, e) in enumerate(intervals):
            if x > e:
                ans.append([b, e])
            elif y < b:
                ans.append([x, y])
                return ans+intervals[i:]
            else:
                x = min(x, b)
                y = max(y, e)
        return ans+[[x, y]]  # meaning [x, y] is the last one
# @lc code=end

