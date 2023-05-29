# TC: O(n*size)  SC: O(n*size)
def normal_bag_2d(weight, value, size):
    n = len(weight)
    dp = [[0] * (size+1) for _ in range(n)]
    for i in range(n):
        for j in range(size+1):
            dp[i][j] = dp[i-1][j]
            if j >= weight[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i]]+value[i])
    return dp[-1][-1]

# TC: O(n*size)  SC: O(size)
def normal_bag_1d(weight, value, size):
    n = len(weight)
    dp = [0] * (size+1)
    for i in range(n):
        for j in range(size, -1, -1): # reversed order
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return dp[-1]

# TC: O(n*size)  SC: O(n*size)
def complete_bag_2d(weight, value, size):
    n = len(weight)
    dp = [[0] * (size+1) for _ in range(n)]
    for i in range(n):
        for j in range(size+1):
            dp[i][j] = dp[i-1][j]
            if j >= weight[i]:
                dp[i][j] = max(dp[i][j], dp[i][j-weight[i]]+value[i])
    return dp[-1][-1]

# TC: O(n*size)  SC: O(size)
def complete_bag_1d(weight, value, size):
    n = len(weight)
    dp = [0] * (size+1)
    for i in range(n):
        for j in range(size+1): # normal order
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return dp[-1]

print(normal_bag_2d([1,3,2,4], [3,2,1,6], 5))
print(normal_bag_1d([1,3,2,4], [3,2,1,6], 5))
print(complete_bag_2d([1,3,2,4], [3,2,1,6], 5))
print(complete_bag_1d([1,3,2,4], [3,2,1,6], 5))