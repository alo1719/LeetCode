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
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a=[0]*10002
        max=0
        ans=[]
        tmp=[]
        for itv in intervals:
            b=itv[0]
            e=itv[1]
            if e>max: max=e
            if b==e: tmp.append([b,e])
            for i in range(b,e):
                a[i]=1
        for tmpi in tmp:
            b=tmpi[0]
            if b==0 and a[b]==0 and [b,b] not in ans: ans.append([b,b])
            if b!=0 and a[b]==0 and a[b-1]==0 and [b,b] not in ans: ans.append([b,b])
        inrange=False
        for i in range(0,max+2):
            if a[i]==1 and not inrange:
                b=i
            if a[i]==0 and inrange:
                e=i
                ans.append([b,e])
            if a[i]==1: inrange=True
            else: inrange=False
        print(ans)
        return ans
# @lc code=end
