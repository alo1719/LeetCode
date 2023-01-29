def solve(s, n, x, y):
    MOD = 10 ** 9 + 7
    prev_same = [0] * len(s)
    l, r = -1, -1
    for i in range(len(s)):
        if s[i] == 'l':
            prev_same[i] = l
            l = i
        else:
            prev_same[i] = r
            r = i
    
    dp = [[0] * (n + 1) for _ in range(len(s) + 1)]
    dp[0][x] = 1
    for i in range(1, len(s) + 1):
        for j in range(n + 1):
            dp[i][j] = dp[i - 1][j]
            if (s[i - 1] == 'l'):
                if j + 1 <= n:
                    dp[i][j] += dp[i - 1][j + 1]
                if j + 1 <= n and prev_same[i - 1] >= 0:
                    dp[i][j] -= dp[prev_same[i - 1]][j + 1]
            else:
                if j - 1 >= 0:
                    dp[i][j] += dp[i - 1][j - 1]
                if j - 1 >= 0 and prev_same[i - 1] >= 0:
                    dp[i][j] -= dp[prev_same[i - 1]][j - 1]
            dp[i][j] = (dp[i][j] + MOD) % MOD
    return dp[len(s)][y]

print(solve('rrlrlr', 6, 1, 3))
print(solve('rrrlrr', 7, 0, 0))