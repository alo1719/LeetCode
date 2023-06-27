#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/
#
# algorithms
# Hard (45.79%)
# Likes:    8392
# Dislikes: 159
# Total Accepted:    491.1K
# Total Submissions: 1.1M
# Testcase Example:  '[3,3,5,0,0,3,1,4]'
#
# You are given an array prices where prices[i] is the price of a given stock
# on the i^th day.
# 
# Find the maximum profit you can achieve. You may complete at most two
# transactions.
# 
# Note: You may not engage in multiple transactions simultaneously (i.e., you
# must sell the stock before you buy again).
# 
# 
# Example 1:
# 
# 
# Input: prices = [3,3,5,0,0,3,1,4]
# Output: 6
# Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit =
# 3-0 = 3.
# Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 =
# 3.
# 
# Example 2:
# 
# 
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit =
# 5-1 = 4.
# Note that you cannot buy on day 1, buy on day 2 and sell them later, as you
# are engaging multiple transactions at the same time. You must sell before
# buying again.
# 
# 
# Example 3:
# 
# 
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transaction is done, i.e. max profit = 0.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= prices.length <= 10^5
# 0 <= prices[i] <= 10^5
# 
# 
#

# @lc code=start
# TC: O(n)  SC: O(n)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        @cache
        def f(i, t, bought):
            if i == n or (t == 2 and not bought): return 0
            buy = f(i+1, t+1, True)-prices[i] if not bought else 0
            hold = f(i+1, t, bought)
            sell = f(i+1, t, False)+prices[i] if bought else 0
            return max(buy, hold, sell)

        n = len(prices)
        return f(0, 0, False)
# @lc code=end

