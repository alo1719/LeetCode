# The data analysts of Hackerland want to schedule some long-running tasks on remote servers optimally to minimize the cost of running them locally. The analysts have two servers, a paid one and a free one. The free server can be used only if the paid server is occupied.

# The ith task is expected to take time[i] units of time to complete and the cost of processing the task on the paid server is cost[i]. The task can be run on the free server only if some task is already running on the paid server. The cost of the free server is 0 and it can process any task in 1 unit of time.

# Find the minimum cost to complete all the tasks if tasks are scheduled optimally.

# dp[i][j]: at i-th task, with j time "credit", the minimum cost to complete all i tasks
# note that j can be negative, but when i = n-1, j needs to be non-negative to be a valid answer
# dp[i][j] = min(dp[i-1][j-time[i]]+cost[i], dp[i-1][j+1])
# since j can be negative, shift j by n to make it all non-negative
# and it does not make sense to have add j when j is already >= n
# so j's range is [-n, n+max(time)] => [0, 2n+max(time)]

# TC: O(n^2)  SC: O(n)
def task_scheduling(cost, time):
    n = len(cost)
    dp = [float('inf')] * (2*n+max(time)+1)
    dp[n] = 0
    for i in range(n):
        prev = dp
        dp = [float('inf')] * (2*n+max(time)+1)
        for j in range(2*n+max(time)):
            dp[j] = prev[j+1]
            if j >= time[i]:
                dp[j] = min(prev[j-time[i]]+cost[i], dp[j])
    return min(dp[n::])

print(task_scheduling([1,2,3,2], [1,2,3,2])==3)
print(task_scheduling([2,3,4,2], [1,1,1,1])==4)
print(task_scheduling([1,1,1,1,1,1], [1,1,1,1,1,1])==3)
print(task_scheduling([4], [2])==4)
