# i represents the index of the current task we are considering.
# j represents the number of 0-cost-tasks we are allowed to pick at any point.
# At each point in the function we have two options:

# place the task represented by i in paid server: in this case we add its cost i.e cost[i]
# and earn ourselves time[i] more 0-cost-task credits.
# place it in free server: use-up 1 0-cost-task credit i.e reduce j by 1.
# In the second case we should have checked whether we even have any 0-cost-task credits
# to use. Since we didn't do that, we are checking in the end(i==n) whether our j is negative.
# If it is negative, then it means that the choices we took so far are invalid. Therefore we
# return infinity for this case to avoid it from picked up in min-cost calculation.
def solution(cost, time):
    n = len(cost)
    # Can be done in max(time) * 2 + len(time)
    # DP size is time
    v = max(time) * 2 + n
    dp = [float('inf')] * v
    dp[0] = 0
    for i in range(n):
        for j in range(v - 1, time[i], -1):
            dp[j] = min(dp[j], dp[j - time[i] - 1] + cost[i])
    print(dp)
    # have no idea why it's correct, but it is
    return min(dp[n::])

print(solution([1,2,3,2], [1,2,3,2])==3)
print(solution([2,3,4,2], [1,1,1,1])==4)
print(solution([1,1,1,1,1,1], [1,1,1,1,1,1])==3)
print(solution([4], [2])==4)
