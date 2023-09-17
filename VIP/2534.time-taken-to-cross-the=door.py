from collections import *

# TC: O(n)  SC: O(n)
def timeTaken(arrival, state):
    n = len(arrival)
    ans = [0]*n
    q0 = deque()
    q1 = deque()
    time = -1
    prev = -1
    i = 0
    while i < n or q0 or q1:
        time += 1
        while i < n and time == arrival[i]:
            if state[i] == 0:
                q0.append(i)
            else:
                q1.append(i)
            i += 1
        if q0 and q1:
            if prev == -1 or prev == 1:
                prev = 1
                ans[q1.popleft()] = time
            elif prev == 0:
                ans[q0.popleft()] = time
        elif not q0 and not q1:
            prev = -1
        elif q0:
            prev = 0
            ans[q0.popleft()] = time
        else:
            prev = 1
            ans[q1.popleft()] = time
    return ans

print(timeTaken([0,1,1,2,4], [0,1,0,0,1]))
print(timeTaken([0,0,0], [1,0,1]))