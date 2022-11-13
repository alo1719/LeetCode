# Expedia OA2
def countGoodStrings(min_length, max_length, one_group, zero_group):
    dp = [0] * (max_length + 1)
    dp[one_group] = 1
    dp[zero_group] = 1
    for i in range(max(one_group, zero_group), max_length + 1):
        dp[i] += dp[i - one_group] if i >= one_group else 0
        dp[i] += dp[i - zero_group] if i >= zero_group else 0
        dp[i] %= 1000000007
    print(dp)
    return sum(dp[min_length:max_length + 1]) % 1000000007


if __name__ == '__main__':
    print(countGoodStrings(2, 7, 3, 2))