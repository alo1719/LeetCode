from collections import *
from functools import *


# TC: O(nlogn)  SC: O(n)
def process_execution(nums):
    # f[i] = max(f[i+1], d[dk[i]]+(f[i+1] if dk[i+1] != dk[i]+1 else f[i+2]))
    @cache
    def f(i):
        if i == n-1: return d[dk[i]]
        if i >= n: return 0
        not_choose = f(i+1)
        choose = d[dk[i]]
        choose += f(i+1) if dk[i+1] != dk[i]+1 else f(i+2)
        return max(not_choose, choose)
    d = defaultdict(int)
    for num in nums: d[num] += num
    dk = sorted(d.keys())
    n = len(dk)
    return f(0)

print(process_execution([1,2,2,3,3,3,8]))  # 18
print(process_execution([0,1,2,2,3,3,3,8]))  # 18
print(process_execution([0,1,2,2,2,2,3,3,8]))  # 16