#
# @lc app=leetcode.cn id=1658 lang=python3
#
# [1658] Minimum Operations to Reduce X to Zero
#
# https://leetcode.cn/problems/minimum-operations-to-reduce-x-to-zero/description/
#
# algorithms
# Medium (39.07%)
# Likes:    260
# Dislikes: 0
# Total Accepted:    34.5K
# Total Submissions: 88.4K
# Testcase Example:  '[1,1,4,2,3]\n5'
#
# You are given an integer array nums and an integer x. In one operation, you
# can either remove the leftmost or the rightmost element from the array nums
# and subtract its value from x. Note that this modifies the array for future
# operations.
# 
# Return the minimum number of operations to reduce x to exactly 0 if it is
# possible, otherwise, return -1.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,4,2,3], x = 5
# Output: 2
# Explanation: The optimal solution is to remove the last two elements to
# reduce x to zero.
# 
# 
# Example 2:
# 
# 
# Input: nums = [5,6,7,8,9], x = 4
# Output: -1
# 
# 
# Example 3:
# 
# 
# Input: nums = [3,2,20,1,1,3], x = 10
# Output: 5
# Explanation: The optimal solution is to remove the last three elements and
# the first two elements (5 operations in total) to reduce x to zero.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# 1 <= nums[i] <= 10^4
# 1 <= x <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    # sliding window
    def minOperations(self, nums: List[int], x: int) -> int:
        sum_nums = sum(nums)
        goal = sum_nums - x
        n = len(nums)
        now = 0
        ans = -1
        left = 0
        for right in range(n):
            now += nums[right]
            while (now > goal and left < n):
                now -= nums[left]
                left += 1
            if now == goal:
                ans = max(ans, right - left + 1)
        return n - ans if ans != -1 else -1
    
class Solution:
    # prefix & postfix sum
    def minOperations(self, nums: List[int], x: int) -> int:
        sum = 0
        n = len(nums)
        prefix = [0] * n
        for i in range(n):
            sum += nums[i]
            prefix[i] = sum
        sum = 0
        postfix = {}
        for i in range(n - 1, -1, -1):
            sum += nums[i]
            postfix[sum] = i
        postfix[0] = n
        ans = float("inf")
        for i in range(-1, n):
            latter_part = x - prefix[i] if i >=0 else x
            if latter_part in postfix and postfix[latter_part] > i:
                ans = min(ans, (i + 1) + (n - postfix[latter_part]))
        return ans if ans != float("inf") else -1
# @lc code=end

