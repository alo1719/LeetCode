# TC: O(n^2 logn)  SC: O(n^2)
# https://leetcode.com/discuss/interview-question/850974/hackerrank-online-assessment-roblox-new-grad-how-to-solve-this
def largest_subgrid(grid, max_sum) -> int:
    # O(n^2) - worst case when k = 1, there will be n^2 operations
    def maxsum_region(k):
        total = 0
        for i in range(n-k+1):
            for j in range(n-k+1):
                net_sum = f[i+k][j+k]-(f[i][j+k]+f[i+k][j]-f[i][j])
                total = max(total, net_sum)
        return total
    
    if not grid or not grid[0]: return 0

    # create culmulative sum 2d array. O(n^2) pre computation
    # f[i][j] = f[i-1][j]+f[i][j-1]-f[i-1][j-1]+grid[i-1][j-1] (f is 1-indexed)
    n = len(grid)
    f = [[0]*(n+1) for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            f[i][j] = f[i-1][j]+f[i][j-1]-f[i-1][j-1]+grid[i-1][j-1]

    # binary search, O(log n) where n is grid size
    left, right = 0, n
    while left < right:
        mid = (left+right+1)//2
        cur_maxsum = maxsum_region(mid)
        if cur_maxsum > max_sum:
            right = mid-1
        else:
            left = mid
    return left

print(largest_subgrid([[1,1,1],[1,1,1],[1,1,1]], 4))  # 2
print(largest_subgrid([[1,1,1,1],[2,2,2,2],[3,3,3,3],[4,4,4,4]], 39))  # 3
print(largest_subgrid([[4,5],[6,7]], 2))  # 0