# https://leetcode.com/discuss/interview-question/850974/hackerrank-online-assessment-roblox-new-grad-how-to-solve-this
def largest_subgrid(grid, max_sum) -> int:
    if not grid or not grid[0]: return 0

    # create culmulative sum 2D array. O(n^2) pre computation
    n = len(grid)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            dp[i][j] = grid[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]

    # O(n^2) - worst case when k = 1, there will be n^2 operations
    def maxsum_region(k):
        total = 0
        for i in range(n - k + 1):
            for j in range(n - k + 1):
                gross_sum = dp[i + k][j + k]  # sum_od
                sum_ob = dp[i][j + k]
                sum_oc = dp[i + k][j]
                sum_oa = dp[i][j]
                net_sum = gross_sum - sum_ob - sum_oc + sum_oa
                total = max(total, net_sum)
        return total

    # binary search. O(log n) where n is grid size
    left, right = 0, n
    while left <= right:
        mid = left + (right - left) // 2
        cur_maxsum = maxsum_region(mid)
        if mid == 0 or mid == n or cur_maxsum <= max_sum < maxsum_region(mid + 1):
            return mid
        elif max_sum > cur_maxsum:
            left = mid + 1
        else:
            right = mid - 1
