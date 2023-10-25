#
# @lc app=leetcode id=956 lang=python3
#
# [956] Tallest Billboard
#
# https://leetcode.com/problems/tallest-billboard/description/
#
# algorithms
# Hard (39.71%)
# Likes:    918
# Dislikes: 29
# Total Accepted:    17.2K
# Total Submissions: 42.6K
# Testcase Example:  '[1,2,3,6]'
#
# You are installing a billboard and want it to have the largest height. The
# billboard will have two steel supports, one on each side. Each steel support
# must be an equal height.
# 
# You are given a collection of rods that can be welded together. For example,
# if you have rods of lengths 1, 2, and 3, you can weld them together to make a
# support of length 6.
# 
# Return the largest possible height of your billboard installation. If you
# cannot support the billboard, return 0.
# 
# 
# Example 1:
# 
# 
# Input: rods = [1,2,3,6]
# Output: 6
# Explanation: We have two disjoint subsets {1,2,3} and {6}, which have the
# same sum = 6.
# 
# 
# Example 2:
# 
# 
# Input: rods = [1,2,3,4,5,6]
# Output: 10
# Explanation: We have two disjoint subsets {2,3,5} and {4,6}, which have the
# same sum = 10.
# 
# 
# Example 3:
# 
# 
# Input: rods = [1,2]
# Output: 0
# Explanation: The billboard cannot be supported, so we return 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= rods.length <= 20
# 1 <= rods[i] <= 1000
# sum(rods[i]) <= 5000
# 
# 
#

# @lc code=start
from functools import cache
from typing import List


class Solution:
    def tallestBillboard(self, rods: List[int]) -> int:
        @cache
        def f(i, acc):
            if i == n: return -inf if acc else 0
            return max(f(i+1, acc+rods[i])+rods[i], f(i+1, acc-rods[i]), f(i+1, acc))
        
        n = len(rods)
        return f(0, 0)
    
print(Solution().tallestBillboard([1,2,3,6]))
# @lc code=end

