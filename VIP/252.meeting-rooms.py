#
# @lc app=leetcode.cn id=252 lang=python3
#
# [252] Meeting Rooms
#
# https://leetcode.cn/problems/meeting-rooms/description/
#
# algorithms
# Easy (57.70%)
# Likes:    140
# Dislikes: 0
# Total Accepted:    22.2K
# Total Submissions: 38.5K
# Testcase Example:  '[[0,30],[5,10],[15,20]]'
#
# Given an array of meeting time intervals where intervals[i] = [starti, endi],
# determine if a person could attend all meetings.
# 
# 
# Example 1:
# Input: intervals = [[0,30],[5,10],[15,20]]
# Output: false
# Example 2:
# Input: intervals = [[7,10],[2,4]]
# Output: true
# 
# 
# Constraints:
# 
# 
# 0 <= intervals.length <= 10^4
# intervals[i].length == 2
# 0 <= starti < endi <= 10^6
# 
# 
#

# @lc code=start
class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        sorted_intervals = sorted(intervals, key=lambda x:x[0])
        if not intervals: return True
        n, last = len(intervals), sorted_intervals[0][1]
        for i in range(1, n):
            print(sorted_intervals[i][1])
            print(last)
            if sorted_intervals[i][0] < last:
                return False
            else:
                last = sorted_intervals[i][1]
        return True
# @lc code=end

