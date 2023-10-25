#
# @lc app=leetcode.cn id=1248 lang=python3
#
# [1248] Count Number of Nice Subarrays
#
# https://leetcode.cn/problems/count-number-of-nice-subarrays/description/
#
# algorithms
# Medium (57.78%)
# Likes:    250
# Dislikes: 0
# Total Accepted:    48.5K
# Total Submissions: 83.9K
# Testcase Example:  '[1,1,2,1,1]\n3'
#
# Given an array of integers nums and an integer k. A continuous subarray is
# called nice if there are k odd numbers on it.
# 
# Return the number of nice sub-arrays.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and
# [1,2,1,1].
# 
# 
# Example 2:
# 
# 
# Input: nums = [2,4,6], k = 1
# Output: 0
# Explanation: There is no odd numbers in the array.
# 
# 
# Example 3:
# 
# 
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 50000
# 1 <= nums[i] <= 10^5
# 1 <= k <= nums.length
# 
#

# @lc code=start
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            if num%2 == 1:
                nums[i] = 1
            else:
                nums[i] = 0
        right_start, right_end, n = -1, -1, len(nums) # [right_start, right_end]
        odd_count = 0
        ans = 0
        for left in range(n):
            if left >= 1:
                odd_count -= nums[left-1]
            while odd_count < k:
                right_start += 1
                if right_start == n: return ans
                odd_count += nums[right_start]
            right_end = right_start
            while right_end+1 <= n-1 and nums[right_end+1] == 0:
                right_end += 1
            ans += right_end-right_start+1
        return ans
# @lc code=end

