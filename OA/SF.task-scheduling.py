from functools import lru_cache as cache

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
def solution(c, t):
    @cache
    def suffix_sum(i):
        return t[i] + suffix_sum(i + 1) if i < len(t) else 0

    @cache
    def f(i, j):

        if j + suffix_sum(i) < 0:
            return float('inf')

        if j >= n - i:
            return 0

        return min(c[i] + f(i + 1, j + t[i]), f(i + 1, j - 1))

    n = len(c)
    return f(0, 0)

print(solution([1,2,3,2], [1,2,3,2]))
print(solution([2,3,4,2], [1,1,1,1]))
