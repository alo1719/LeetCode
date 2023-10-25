#
# @lc app=leetcode id=1681 lang=python3
#
# [1681] Minimum Incompatibility
#
# https://leetcode.com/problems/minimum-incompatibility/description/
#
# algorithms
# Hard (38.05%)
# Likes:    250
# Dislikes: 91
# Total Accepted:    7.3K
# Total Submissions: 19K
# Testcase Example:  '[1,2,1,4]\n2'
#
# You are given an integer array nums​​​ and an integer k. You are asked to
# distribute this array into k subsets of equal size such that there are no two
# equal elements in the same subset.
# 
# A subset's incompatibility is the difference between the maximum and minimum
# elements in that array.
# 
# Return the minimum possible sum of incompatibilities of the k subsets after
# distributing the array optimally, or return -1 if it is not possible.
# 
# A subset is a group integers that appear in the array with no particular
# order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,1,4], k = 2
# Output: 4
# Explanation: The optimal distribution of subsets is [1,2] and [1,4].
# The incompatibility is (2-1) + (4-1) = 4.
# Note that [1,1] and [2,4] would result in a smaller sum, but the first subset
# contains 2 equal elements.
# 
# Example 2:
# 
# 
# Input: nums = [6,3,8,1,3,1,2,2], k = 4
# Output: 6
# Explanation: The optimal distribution of subsets is [1,2], [2,3], [6,8], and
# [1,3].
# The incompatibility is (2-1) + (3-2) + (8-6) + (3-1) = 6.
# 
# 
# Example 3:
# 
# 
# Input: nums = [5,3,3,6,3,3], k = 3
# Output: -1
# Explanation: It is impossible to distribute nums into 3 subsets where no two
# elements are equal in the same subset.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= k <= nums.length <= 16
# nums.length is divisible by k
# 1 <= nums[i] <= nums.length
# 
# 
#

# @lc code=start
class Solution:
    def minimumIncompatibility(self, nums: List[int], k: int) -> int:
        @cache
        def f(mask, last):
            if mask == 0: return 0
            if mask.bit_count()%s == 0:  # new subset
                lowbit = mask&(-mask)
                return f(mask^lowbit, lowbit.bit_length()-1)
            ans = inf
            for j in range(last+1, n):
                if (mask>>j)&1 == 1 and nums[j] > nums[last]:
                    ans = min(ans, nums[j]-nums[last]+f(mask^(1<<j), j))
            return ans
            
        n = len(nums)
        d = defaultdict(int)
        s = n//k
        if s == 1: return 0
        for num in nums:
            d[num] += 1
            if d[num] > n//2: return -1
        nums.sort()
        ans = f((1<<n)-2, 0)  # mask (can select), last number
        return ans if ans != inf else -1
# @lc code=end

