def maxScore(s):
    # double dp approach
    # O(n^2) Soluiton considering len(s)<=3000
    # lets find out first the length of palindromic subsequence for each valid subarray
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    mx_left = [1] * n
    mx_right = [1] * n
    for size in range(1, n+1):
        for l in range(n):
            r = l + size - 1 # [l, r]
            if r < n:
                if size == 1:
                    dp[l][l] = 1
                elif size == 2:
                    if s[l] == s[r]:
                        dp[l][r] = 2
                    else:
                        dp[l][r] = 1
                else:
                    if s[l] == s[r]:
                        dp[l][r] = 2 + dp[l+1][r-1]
                    else:
                        dp[l][r] = max(dp[l][r], dp[l][r-1], dp[l+1][r])

                # capture max len of subsequence in left and right so far for l and r
                # kind of double dp...
                mx_left[r] = max(mx_left[r], dp[l][r])
                mx_right[l] = max(mx_right[l], dp[l][r])
    ans = 0
    for i in range(n-1):
        # consider i has the right end of first subarray
        ans = max(ans, mx_left[i] * mx_right[i+1])
    return ans

print(maxScore("attract"))
print(maxScore("acdapmpomp"))