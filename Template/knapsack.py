from math import inf


# TC: O(n*capacity)  SC: O(n*capacity)
def normal_knapsack_2d(weight, value, capacity):
    n = len(weight)
    dp = [[0]*(capacity+1) for _ in range(n)]
    for i in range(n):
        for j in range(capacity+1):
            dp[i][j] = dp[i-1][j]
            if j >= weight[i]:
                dp[i][j] = max(dp[i][j], dp[i-1][j-weight[i]]+value[i])
    return max(dp[-1])

# TC: O(n*capacity)  SC: O(capacity)
def normal_knapsack_1d(weight, value, capacity):
    n = len(weight)
    dp = [0]*(capacity+1)
    for i in range(n):
        for j in range(capacity, -1, -1):  # reversed order
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return max(dp)

# TC: O(n*capacity)  SC: O(n*capacity)
def complete_knapsack_2d(weight, value, capacity):
    n = len(weight)
    dp = [[0]*(capacity+1) for _ in range(n)]
    for i in range(n):
        for j in range(capacity+1):
            dp[i][j] = dp[i-1][j]
            if j >= weight[i]:
                dp[i][j] = max(dp[i][j], dp[i][j-weight[i]]+value[i])
    return max(dp[-1])

# TC: O(n*capacity)  SC: O(capacity)
def complete_knapsack_1d(weight, value, capacity):
    n = len(weight)
    dp = [0] * (capacity+1)
    for i in range(n):
        for j in range(capacity+1):  # normal order
            if j >= weight[i]:
                dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return max(dp)

# AT LEAST KNAPSACK: at least reach capacity, and minimize the value
def at_least_knapsack(weight, value, capacity):
    n = len(weight)
    dp = [0]+[inf]*capacity
    for i in range(n):
        for j in range(capacity, 0, -1):
            dp[j] = min(dp[j], dp[max(0, j-weight[i])]+value[i])  # max(0, j-weight[i]) to avoid negative index
    return dp[-1]

# JUST KNAPSACK: reach capacity exactly, and maximize/minimize the value
def just_knapsack(weight, value, capacity):
    n = len(weight)
    dp = [0]+[-inf]*capacity  # [inf] for minimize
    for i in range(n):
        for j in range(capacity, weight[i]-1, -1):
            dp[j] = max(dp[j], dp[j-weight[i]]+value[i])
    return dp[-1]  # only change this

print(normal_knapsack_2d([1,3,2,4], [3,2,1,6], 5))
print(normal_knapsack_1d([1,3,2,4], [3,2,1,6], 5))
print(complete_knapsack_2d([1,3,2,4], [3,2,1,6], 5))
print(complete_knapsack_1d([1,3,2,4], [3,2,1,6], 5))
print(at_least_knapsack([1,3,2,4], [3,2,1,6], 5))
print(just_knapsack([1,3,2,4], [3,2,1,6], 5))