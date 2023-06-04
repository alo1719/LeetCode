from collections import deque


# TC: O(n), SC: O(n)
def max_pooling(arr, pool, stride):
    n, dq = len(arr), deque()
    # monotonic queue, store index, decreasing
    # idea is maintaining elements that could potentially be the max
    for i in range(pool):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
    ans = [arr[dq[0]]]
    acc = 0
    for i in range(pool, n):
        while dq and arr[i] >= arr[dq[-1]]:
            dq.pop()
        dq.append(i)
        while dq[0] <= i-pool: # slide over it
            dq.popleft()
        acc += 1
        if acc == stride:
            acc = 0
            ans.append(arr[dq[0]])
    return ans

print(max_pooling([1,2,3,4,5,6,7,8,9,10], 4, 2)) # [4,6,8,10]
print(max_pooling([10,9,8,7,6,5,4,3,2,1], 4, 2)) # [10,8,6,4]
print(max_pooling([54,26,93,17,77,31,44,55,20,1], 4, 2)) # [93,93,77,55]