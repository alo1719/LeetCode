#
# @lc app=leetcode.cn id=370 lang=python3
#
# [370] Range Addition
#
# https://leetcode.cn/problems/range-addition/description/
#
# algorithms
# Medium (76.30%)
# Likes:    150
# Dislikes: 0
# Total Accepted:    11K
# Total Submissions: 14.4K
# Testcase Example:  '5\n[[1,3,2],[2,4,3],[0,2,-2]]'
#
# You are given an integer length and an array updates where updates[i] =
# [startIdxi, endIdxi, inci].
# 
# You have an array arr of length length with all zeros, and you have some
# operation to apply on arr. In the i^th operation, you should increment all
# the elements arr[startIdxi], arr[startIdxi + 1], ..., arr[endIdxi] by inci.
# 
# Return arr after applying all the updates.
# 
# 
# Example 1:
# 
# 
# Input: length = 5, updates = [[1,3,2],[2,4,3],[0,2,-2]]
# Output: [-2,0,3,5,3]
# 
# 
# Example 2:
# 
# 
# Input: length = 10, updates = [[2,4,6],[5,6,8],[1,9,-4]]
# Output: [0,-4,2,2,2,4,4,-4,-4,-4]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= length <= 10^5
# 0 <= updates.length <= 10^4
# 0 <= startIdxi <= endIdxi < length
# -1000 <= inci <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def get_modified_array(self, length: int, updates: List[List[int]]) -> List[int]:
        cumulative = [0] * length
        array = [0] * length
        for update in updates:
            start = update[0]
            end = update[1]
            addition = update[2]
            cumulative[start] += addition
            if end + 1 <= length - 1:
                cumulative[end + 1] -= addition
        sum = 0
        for i in range(length):
            sum += cumulative[i]
            array[i] = sum
        return array
# @lc code=end
