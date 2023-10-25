#
# @lc app=leetcode.cn id=718 lang=python3
#
# [718] Maximum Length of Repeated Subarray
#
# https://leetcode.cn/problems/maximum-length-of-repeated-subarray/description/
#
# algorithms
# Medium (57.14%)
# Likes:    811
# Dislikes: 0
# Total Accepted:    160.5K
# Total Submissions: 280.9K
# Testcase Example:  '[1,2,3,2,1]\n[3,2,1,4,7]'
#
# Given two integer arrays nums1 and nums2, return the maximum length of a
# subarray that appears in both arrays.
# 
# 
# Example 1:
# 
# 
# Input: nums1 = [1,2,3,2,1], nums2 = [3,2,1,4,7]
# Output: 3
# Explanation: The repeated subarray with maximum length is [3,2,1].
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [0,0,0,0,0], nums2 = [0,0,0,0,0]
# Output: 5
# Explanation: The repeated subarray with maximum length is [0,0,0,0,0].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length <= 1000
# 0 <= nums1[i], nums2[i] <= 100
# 
# 
#

# @lc code=start
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # 1. DP, equivalent to longest common substr
        # m, n = len(nums1), len(nums2)
        # dp = [[0]*(n+1) for _ in range(m+1)]
        # ans = 0
        # for i in range(m):
        #     for j in range(n):
        #         if nums1[i] == nums2[j]:
        #             dp[i+1][j+1] = dp[i][j]+1
        #             ans = max(ans, dp[i+1][j+1])
        # return ans
        # 2. Sliding Window
        # str1 = "".join([chr(ch) for ch in nums1])
        # str2 = "".join([chr(ch) for ch in nums2])
        # ans, max_str = 0, ""
        # for ch in str1:
        #     max_str += ch
        #     if max_str in str2:
        #         ans = max(ans, len(max_str))
        #     else:
        #         max_str = max_str[1:]
        # return ans
        # 3. Hash (rabin-karp) + Binary search
        def check_valid(length):
            max_length = max(len(str1), len(str2))
            if length <= 0: return True
            str1_hash_set = set()
            for i in range(len(str1)-length+1):
                last_hash_value = 0 if i == 0 else str1_hash[i-1]
                cur_hash = (str1_hash[i+length-1]-last_hash_value+m)%m
                final_hash = (cur_hash*p_pow[max_length-length-i])%m
                str1_hash_set.add(final_hash)
            for i in range(len(str2)-length+1):
                last_hash_value = 0 if i == 0 else str2_hash[i-1]
                cur_hash = (str2_hash[i+length-1]-last_hash_value+m)%m
                final_hash = (cur_hash*p_pow[max_length-length-i])%m
                if final_hash in str1_hash_set: return True
            return False
        
        
        str1 = "".join([chr(ch) for ch in nums1])
        str2 = "".join([chr(ch) for ch in nums2])
        p, m = 101, 10**9+9
        p_pow = [1]*max(len(str1), len(str2))
        str1_hash = [0]*len(str1)
        str2_hash = [0]*len(str2)
        for i in range(1, len(p_pow)):
            p_pow[i] = (p_pow[i-1]*p)%m
        for i in range(len(str1)):
            last_hash_value = 0 if i == 0 else str1_hash[i-1]
            str1_hash[i] = (last_hash_value+(ord(str1[i]))*p_pow[i])%m
        for i in range(len(str2)):
            last_hash_value = 0 if i == 0 else str2_hash[i-1]
            str2_hash[i] = (last_hash_value+(ord(str2[i]))*p_pow[i])%m
        left, right = 0, min(len(nums1), len(nums2))
        ans = 0
        while left <= right:
            mid = (left+right)//2
            if check_valid(mid):
                ans = mid
                left = mid+1
            else:
                right = mid-1
        return ans
# @lc code=end

