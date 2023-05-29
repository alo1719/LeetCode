# "attract" palindromic subsequences: [a,t,r,c,aa,tt,ata,ara,ttt,trt,tat,tct,atta]
# 2 non-overlapping palindromic with maximum product is |atta| * |c| (or |t|) = 4
# notice that r cannot be chosen because it's before a
# TC: O(n^2)  SC: O(n^2) (can be optimized to O(n))
def maxScore(s):
    ans, n = 0, len(s)
    dp = [[0] * n for _ in range(n)] # dp[i][j] means s[i] to s[j] palindrome subsequence max length
    max_left = [1] * n
    max_right = [1] * n
    for i in range(n-1, -1, -1):
        dp[i][i] = 1
        for j in range(i+1, n):
            if j == i+1 and s[i] == s[j]:
                dp[i][j] = 2
            elif dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] = 2+dp[i+1][j-1]
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
            max_left[j] = max(max_left[j], dp[i][j])
            max_right[i] = max(max_right[i], dp[i][j])
    for i in range(n-1):
        ans = max(ans, max_left[i] * max_right[i+1])
    return ans

print(maxScore("attract")) # atta c
print(maxScore("acdapmpomp")) # ada pmpmp