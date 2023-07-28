from collections import defaultdict
from math import *

# TC: O(n)  SC: O(26*n)
def doordash(s1, s2):
    m, n = len(s1), len(s2)
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    jump = [defaultdict(lambda:-1) for _ in range(m)]
    for i in range(m-2, -1, -1):
        for ch in str:
            if s1[i+1] == ch:
                jump[i][ch] = i+1
            else:
                jump[i][ch] = jump[i+1][ch]
    # f[i] = jump[f[i-1]][s2[i]]
    f = [-1 for _ in range(n)]
    for i in range(n):
        if i == 0:
            f[i] = s1.find(s2[i])
        else:
            f[i] = jump[f[i-1]][s2[i]]
        if f[i] == -1: break
    rjump = [defaultdict(lambda:-1) for _ in range(m)]
    for i in range(1, m):
        for ch in str:
            if s1[i-1] == ch:
                rjump[i][ch] = i-1
            else:
                rjump[i][ch] = rjump[i-1][ch]
    rf = [-1 for _ in range(n)]
    for i in range(n-1, -1, -1):
        if i == n-1:
            rf[i] = s1.rfind(s2[i])
        else:
            rf[i] = rjump[rf[i+1]][s2[i]]
        if rf[i] == -1: break

    # sliding window
    ans = n
    left = 0
    for right in range(n+1):  # delete [left, right)
        rval = rf[right] if right != n else inf
        if rval == -1: continue
        while left+1 <= right and f[left] != -1 and f[left] < rval:
            left += 1
        ans = min(ans, right-left)
    return ans

# remove [l, r] from s2, make s2 sub-sequence of s1, ask minimum of r-l+1
print(doordash("HACKERRANK", "HACKERMAN"))  # 1
print(doordash("ABACABA", "ABA"))  # 0
print(doordash("ABA", "ABACCA"))  # 3
print(doordash("ABA", "ABAD"))  # 1
print(doordash("ABA", "ABA"))  # 0
print(doordash("CCABA", "ABA"))  # 0
print(doordash("ABACC", "ABA"))  # 0
print(doordash("ABA", "CCABA"))  # 2
print(doordash("ABA", "ABACC"))  # 2
