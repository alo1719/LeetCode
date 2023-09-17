from collections import *

# TC: O(n)  SC: O(n)
def maximum_distinct(a, b, k):
    m = len(a)
    ca = Counter(a)
    la = len(ca)
    cb = Counter(b)
    diff = 0
    for be in cb:
        if be not in ca:
            diff += 1
    return min(m, la+min(diff, k))
    
print(maximum_distinct([2,3,3,2,2],[1,3,2,4,1],2))  # 4
print(maximum_distinct([1,1,4,5,5],[4,4,3,1,5],2))  # 4
print(maximum_distinct([1,2,3],[4,5,6],5))  # 3
