#
# @lc app=leetcode.cn id=904 lang=python3
#
# [904] Fruit Into Baskets
#
# https://leetcode.cn/problems/fruit-into-baskets/description/
#
# algorithms
# Medium (45.36%)
# Likes:    430
# Dislikes: 0
# Total Accepted:    111.2K
# Total Submissions: 245.1K
# Testcase Example:  '[1,2,1]'
#
# You are visiting a farm that has a single row of fruit trees arranged from
# left to right. The trees are represented by an integer array fruits where
# fruits[i] is the type of fruit the i^th tree produces.
# 
# You want to collect as much fruit as possible. However, the owner has some
# strict rules that you must follow:
# 
# 
# You only have two baskets, and each basket can only hold a single type of
# fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from
# every tree (including the start tree) while moving to the right. The picked
# fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must
# stop.
# 
# 
# Given the integer array fruits, return the maximum number of fruits you can
# pick.
# 
# 
# Example 1:
# 
# 
# Input: fruits = [1,2,1]
# Output: 3
# Explanation: We can pick from all 3 trees.
# 
# 
# Example 2:
# 
# 
# Input: fruits = [0,1,2,2]
# Output: 3
# Explanation: We can pick from trees [1,2,2].
# If we had started at the first tree, we would only pick from trees [0,1].
# 
# 
# Example 3:
# 
# 
# Input: fruits = [1,2,3,2,2]
# Output: 4
# Explanation: We can pick from trees [2,3,2,2].
# If we had started at the first tree, we would only pick from trees [1,2].
# 
# 
# 
# Constraints:
# 
# 
# 1 <= fruits.length <= 10^5
# 0 <= fruits[i] < fruits.length
# 
# 
#

# @lc code=start
from collections import defaultdict


class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding window
        left, right, n, ans = 0, -1, len(fruits), 0
        basket_dict = defaultdict(int)
        for left in range(n): # [left, right]
            if left >= 1:
                basket_dict[fruits[left - 1]] -= 1
                if basket_dict[fruits[left - 1]] == 0:
                    del basket_dict[fruits[left - 1]]
            while right + 1 < n and (len(basket_dict) < 2 or fruits[right + 1] in basket_dict):
                right += 1
                basket_dict[fruits[right]] += 1
                if right - left + 1 > ans: ans = right - left + 1
        return ans
# @lc code=end

