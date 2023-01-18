import collections

def dd(s1, s2):
    jump = [collections.defaultdict(lambda :-1) for _ in range(len(s1))]
    str = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in range(len(s1) - 2, -1, -1):
        for j in str:
            if s1[i + 1] == j:
                jump[i][j] = i + 1
            else:
                jump[i][j] = jump[i + 1][j]
    f = [-1 for _ in range(len(s2))]
    f[0] = s1.find(s2[0])
    if f[0] != -1:
        for i in range(1, len(f)):
            f[i] = jump[f[i - 1]][s2[i]]
            if f[i] == -1:
                break
    print(f)
    jump_reverse = [collections.defaultdict(lambda :-1) for _ in range(len(s1))]
    for i in range(1, len(s1)):
        for j in str:
            if s1[i - 1] == j:
                jump_reverse[i][j] = i - 1
            else:
                jump_reverse[i][j] = jump_reverse[i - 1][j]
    # print(jump_reverse)
    g = [-1 for _ in range(len(s2))]
    g[-1] = s1.rfind(s2[-1])
    if g[-1] != -1:
        for i in range(len(g) - 2, -1, -1):
            g[i] = jump_reverse[g[i + 1]][s2[i]]
            if g[i] == -1:
                break
    print(g)
    g_available = []
    for i, g_element in enumerate(g):
        if g_element != -1:
            g_available.append(i)
    g_available.append(len(s2)) # add a dummy element
    ans = len(s2)
    r = len(g_available) - 1
    print(g_available)
    for l in range(len(s2) - 1, -1, -1):
        if f[l] == -1: continue
        while r - 1 >= 0 and g_available[r - 1] > l and g[g_available[r - 1]] > f[l]:
            r -= 1
        ans = min(g_available[r] - l - 1, ans)
    print(ans)
    return ans

# remove [l, r] from s2, make s2 sub-sequence of s1, ask minimum of r-l+1
dd("HACKERRANK", "HACKERMAN")
dd("ABACABA", "ABA")
dd("ABA", "ABACCA")
dd("ABA", "ABAD")