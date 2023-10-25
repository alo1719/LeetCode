#
# @lc app=leetcode id=2448 lang=python3
#
# [2448] Minimum Cost to Make Array Equal
#
# https://leetcode.com/problems/minimum-cost-to-make-array-equal/description/
#
# algorithms
# Hard (45.92%)
# Likes:    2296
# Dislikes: 33
# Total Accepted:    61.8K
# Total Submissions: 134.5K
# Testcase Example:  '[1,3,5,2]\n[2,3,1,14]'
#
# You are given two 0-indexed arrays nums and cost consisting each of n
# positive integers.
# 
# You can do the following operation any number of times:
# 
# 
# Increase or decrease any element of the array nums by 1.
# 
# 
# The cost of doing one operation on the i^th element is cost[i].
# 
# Return the minimum total cost such that all the elements of the array nums
# become equal.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,3,5,2], cost = [2,3,1,14]
# Output: 8
# Explanation: We can make all the elements equal to 2 in the following way:
# - Increase the 0^th element one time. The cost is 2.
# - Decrease the 1^st element one time. The cost is 3.
# - Decrease the 2^nd element three times. The cost is 1 + 1 + 1 = 3.
# The total cost is 2 + 3 + 3 = 8.
# It can be shown that we cannot make the array equal with a smaller cost.
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,2,2,2,2], cost = [4,2,8,1,3]
# Output: 0
# Explanation: All the elements are already equal, so no operations are
# needed.
# 
# 
# 
# Constraints:
# 
# 
# n == nums.length == cost.length
# 1 <= n <= 10^5
# 1 <= nums[i], cost[i] <= 10^6
# Test cases are generated in a way that the output doesn't exceed 2^53-1
# 
# 
#

# @lc code=start
class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        n = len(nums)
        minn = min(nums)
        maxx = max(nums)
        left, right = minn, maxx
        while left < right:
            # print(left, right)
            mid_left = (left+right)//2
            mid_right = (left+right)//2+1
            tmp_left = tmp_right = 0
            for i in range(n):
                tmp_left += cost[i]*abs(mid_left-nums[i])
                tmp_right += cost[i]*abs(mid_right-nums[i])
            if tmp_left < tmp_right:
                right = mid_left
            else:
                left = mid_right
        return sum([cost[i]*abs(left-nums[i]) for i in range(n)])
# @lc code=end

