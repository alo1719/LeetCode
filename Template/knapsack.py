from math import inf


# TC: O(n*capacity)  SC: O(n*capacity)
def normal_knapsack_2d(weight, value, capacity):
    # f[i][w] = max(f[i-1][w], f[i-1][w-weight[i]]+value[i])
    n = len(weight)
    f = [[0]*(capacity+1) for _ in range(n)]
    for i in range(n):
        for w in range(capacity+1):
            f[i][w] = f[i-1][w]
            if w >= weight[i]:
                f[i][w] = max(f[i][w], f[i-1][w-weight[i]]+value[i])
    return max(f[-1])

# TC: O(n*capacity)  SC: O(capacity)
def normal_knapsack_1d(weight, value, capacity):
    n = len(weight)
    f = [0]*(capacity+1)
    for i in range(n):
        for w in range(capacity, weight[i]-1, -1):  # reversed order
            f[w] = max(f[w], f[w-weight[i]]+value[i])
    return max(f)

# TC: O(n*capacity)  SC: O(n*capacity)
def complete_knapsack_2d(weight, value, capacity):
    # f[i][w] = max(f[i-1][w], f[i][w-weight[i]]+value[i])
    n = len(weight)
    f = [[0]*(capacity+1) for _ in range(n)]
    for i in range(n):
        for w in range(capacity+1):
            f[i][w] = f[i-1][w]
            if w >= weight[i]:
                f[i][w] = max(f[i][w], f[i][w-weight[i]]+value[i])
    return max(f[-1])

# TC: O(n*capacity)  SC: O(capacity)
def complete_knapsack_1d(weight, value, capacity):
    n = len(weight)
    f = [0]*(capacity+1)
    for i in range(n):
        for j in range(weight[i], capacity+1):  # normal order
            f[j] = max(f[j], f[j-weight[i]]+value[i])
    return max(f)

# AT LEAST KNAPSACK: at least reach capacity, and minimize the value
def at_least_knapsack(weight, value, capacity):
    # f[i][w] = min(f[i-1][w], f[i-1/i][max(0, w-weight[i])]+value[i])
    n = len(weight)
    f = [0]+[inf]*capacity
    for i in range(n):
        for w in range(capacity, 0, -1):  # reverse order: normal knapsack, normal order: complete knapsack
            f[w] = min(f[w], f[max(0, w-weight[i])]+value[i])  # max(0, j-weight[i]) to avoid negative index
    return f[-1]

# JUST KNAPSACK: reach capacity exactly, and maximize/minimize the value
def just_knapsack(weight, value, capacity):
    n = len(weight)
    f = [0]+[-inf]*capacity  # [inf] for minimize, change #1
    for i in range(n):
        for w in range(capacity, weight[i]-1, -1):  # normal order for complete knapsack
            f[w] = max(f[w], f[w-weight[i]]+value[i])
    return f[-1]  # change #2

print(normal_knapsack_2d([1,3,2,4], [3,2,1,6], 5))  # 9
print(normal_knapsack_1d([1,3,2,4], [3,2,1,6], 5))  # 9
print(normal_knapsack_2d([2,3,2,4], [3,2,1,8], 5))  # 8
print(normal_knapsack_1d([2,3,2,4], [3,2,1,8], 5))  # 8
print(complete_knapsack_2d([1,3,2,4], [3,2,1,6], 5))  # 15
print(complete_knapsack_1d([1,3,2,4], [3,2,1,6], 5))  # 15
print(at_least_knapsack([1,3,2,4], [3,2,1,6], 5))  # 3
print(at_least_knapsack([1,3,2,4], [3,2,1,1], 5))  # 2
print(just_knapsack([1,3,2,4], [3,2,1,6], 6))  # 7
print(just_knapsack([1,3,2,4], [5,2,2,6], 6))  # 9