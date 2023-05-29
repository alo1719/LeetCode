from collections import defaultdict

# TC: O(n)  SC: O(1), ignore digit length
def count_digit_sum_naive(fromm, to):
    buckets = [0] * 200
    for i in range(fromm, to+1):
        acc = 0
        for ch in str(i):
            acc += ord(ch)-ord('0')
        buckets[acc] += 1
    return buckets[1:20]

# dp[i][j]: at i-th digit (1-indexed), with j digit sum, the number of ways to get it (all digit can be 0~9)
# dp[i][j] = sum(dp[i-l][j-k]) l: 1~i-1, k: 1~9, if j-k == 0, only add once
def count_N_9_digit_sum(N):
    sum_dict = defaultdict(int)
    dp = [[0] * (9*N+1) for _ in range(N+1)]
    for i in range(10): dp[1][i] = 1
    for i in range(N+1): dp[i][0] = 1
    for i in range(2, N+1):
        for j in range(1, 9*i+1):
            for k in range(1, 10): # current digit can be 1~9
                for l in range(1, i): # how many 0 to add (transferred from which digit)
                    if j-k > 0:
                        dp[i][j] += dp[i-l][j-k]
                    elif j-k == 0:
                        dp[i][j] += dp[i-l][j-k]
                        break # 000 and 00 and 0 are the same
    for i in range(1, N+1):
        for j in range(9*N+1):
            sum_dict[j] += dp[i][j]
    sum_dict[0] = 1 # again, 000 and 00 and 0 are the same
    return sum_dict

def count_digit_sum_1_by_1(digit_already, lenn, sum_dict):
    if lenn == 0: # no more digit to add
        sum_dict[digit_already] += 1
        return
    N_sum = count_N_9_digit_sum(lenn)
    for k, v in N_sum.items():
        sum_dict[k+digit_already] += v

# 324: 0XX, 1XX, 2XX -> first digit
# 324: 00X, 01X -> second digit
# 324: 000, 001, 002, 003, 004 -> last digit
def count_digit_sum_to(to):
    sum_dict = defaultdict(int)
    for i, ch in enumerate(str(to)):
        digit = ord(ch)-ord('0') # ith digit
        for j in range(digit if i != len(str(to))-1 else digit+1): # j: from 0 to digit-1 unless last one
            before_ith_sum = 0
            for ch_before in str(to)[:i]:
                before_ith_sum += ord(ch_before)-ord('0')
            count_digit_sum_1_by_1(j+before_ith_sum, len(str(to))-i-1, sum_dict)
    return sum_dict

# Overall TC: O(1)  Overall SC: O(1), ignore digit length
# VERY HARD
def count_digit_sum_from_to(fromm, to):
    sum_dict_to = count_digit_sum_to(to)
    sum_dict_fr = count_digit_sum_to(fromm-1)
    for k in sum_dict_fr:
        sum_dict_to[k] -= sum_dict_fr[k]
    return sum_dict_to

print(count_digit_sum_naive(34, 65782))
print(list(count_digit_sum_from_to(34, 65782).values())[1:20])
