#
# @lc app=leetcode.cn id=309 lang=python3
#
# [309] Best Time to Buy and Sell Stock with Cooldown
#
# https://leetcode.cn/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/
#
# algorithms
# Medium (64.01%)
# Likes:    1437
# Dislikes: 0
# Total Accepted:    238.8K
# Total Submissions: 372.8K
# Testcase Example:  '[1,2,3,0,2]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete as many
# transactions as you like (i.e., buy one and sell one share of the stock
# multiple times) with the following restrictions:
# 
# 
# After you sell your stock, you cannot buy stock on the next day (i.e.,
# cooldown one day).
# 
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [1,2,3,0,2]
# Output: 3
# Explanation: transactions = [buy, sell, cooldown, buy, sell]
# 
# 
# Example 2:
# 
# 
# Input: prices = [1]
# Output: 0
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 5000
# 0 <= prices[i] <= 1000
# 
# 
#

# @lc code=start
# WeRide VOE
# TC: O(n)  SC: O(n) (O(1) followup)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def f(i, bought):
            if i >= n: return 0
            if bought: return max(f(i+2, False)+prices[i], f(i+1, True))
            else: return max(f(i+1, False), f(i+1, True)-prices[i])
        n = len(prices)
        return f(0, False)
# @lc code=end

