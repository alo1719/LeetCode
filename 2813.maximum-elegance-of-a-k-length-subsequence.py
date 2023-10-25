#
# @lc app=leetcode.cn id=2813 lang=python3
#
# [2813] Maximum Elegance of a K-Length Subsequence
#
# https://leetcode.cn/problems/maximum-elegance-of-a-k-length-subsequence/description/
#
# algorithms
# Hard (39.08%)
# Likes:    15
# Dislikes: 0
# Total Accepted:    1.5K
# Total Submissions: 3.8K
# Testcase Example:  '[[3,2],[5,1],[10,1]]\n2'
#
# You are given a 0-indexed 2D integer array items of length n and an integer
# k.
# 
# items[i] = [profiti, categoryi], where profiti and categoryi denote the
# profit and category of the i^th item respectively.
# 
# Let's define the elegance of a subsequence of items as total_profit +
# distinct_categories^2, where total_profit is the sum of all profits in the
# subsequence, and distinct_categories is the number of distinct categories
# from all the categories in the selected subsequence.
# 
# Your task is to find the maximum elegance from all subsequences of size k in
# items.
# 
# Return an integer denoting the maximum elegance of a subsequence of items
# with size exactly k.
# 
# Note: A subsequence of an array is a new array generated from the original
# array by deleting some elements (possibly none) without changing the
# remaining elements' relative order.
# 
# 
# Example 1:
# 
# 
# Input: items = [[3,2],[5,1],[10,1]], k = 2
# Output: 17
# Explanation: In this example, we have to select a subsequence of size 2.
# We can select items[0] = [3,2] and items[2] = [10,1].
# The total profit in this subsequence is 3 + 10 = 13, and the subsequence
# contains 2 distinct categories [2,1].
# Hence, the elegance is 13 + 2^2 = 17, and we can show that it is the maximum
# achievable elegance. 
# 
# 
# Example 2:
# 
# 
# Input: items = [[3,1],[3,1],[2,2],[5,3]], k = 3
# Output: 19
# Explanation: In this example, we have to select a subsequence of size 3. 
# We can select items[0] = [3,1], items[2] = [2,2], and items[3] = [5,3]. 
# The total profit in this subsequence is 3 + 2 + 5 = 10, and the subsequence
# contains 3 distinct categories [1,2,3]. 
# Hence, the elegance is 10 + 3^2 = 19, and we can show that it is the maximum
# achievable elegance.
# 
# Example 3:
# 
# 
# Input: items = [[1,1],[2,1],[3,1]], k = 3
# Output: 7
# Explanation: In this example, we have to select a subsequence of size 3. 
# We should select all the items. 
# The total profit will be 1 + 2 + 3 = 6, and the subsequence contains 1
# distinct category [1]. 
# Hence, the maximum elegance is 6 + 1^2 = 7.  
# 
# 
# Constraints:
# 
# 
# 1 <= items.length == n <= 10^5
# items[i].length == 2
# items[i][0] == profiti
# items[i][1] == categoryi
# 1 <= profiti <= 10^9
# 1 <= categoryi <= n 
# 1 <= k <= n
# 
# 
#

# @lc code=start
# TC: O(nlogn)  SC: O(n)
class Solution:
    def findMaximumElegance(self, items: List[List[int]], k: int) -> int:
        # need O(n), not dp, need greedy (acutally regretful greedy)
        # the absolute value is hard to handle, so we compare the **relative value**
        # baseline: sort by profit, ignore category
        # if need to achieve higher elegance:
        # 1. for new item, must choose an unseen category (to potentially increase distinct_categories)
        # 2. (continue 1) must substitude an old item that shown >=2 times
        # 3. (continue 2) then should substitude the old item with the lowest profit
        # in conclusion, for a new item, if it's a new category, then we try to substitude the lowest profit item that
        # has >=2 occurances of the same category.
        items.sort(key=lambda x:x[0], reverse=True)
        ans = total_profit = 0
        vis = set()  # current categories
        dup = []  # profit of items that has >=2 occurances of the same category, because items are decreasingly, dup is also decreasingly
        for i, (profit, category) in enumerate(items):
            if i < k:
                total_profit += profit
                if category not in vis:
                    vis.add(category)
                else:
                    dup.append(profit)
            elif dup and category not in vis:
                vis.add(category)
                total_profit -= dup.pop()
                total_profit += profit
            ans = max(ans, total_profit+len(vis)**2)
        return ans
# @lc code=end

