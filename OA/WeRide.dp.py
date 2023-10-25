from collections import defaultdict
from functools import cache

# TC: O(nlen(n)) = O(nlogn)  SC: O(9*len(n)) = O(logn)
def count_digit_sum_naive(fromm, to):
    buckets = [0]*200
    for i in range(fromm, to+1):
        acc = 0
        for ch in str(i):
            acc += ord(ch)-ord('0')
        buckets[acc] += 1
    return buckets[1:20]

# TC: O(len(n)*9*len(n)*10) = O(lognlogn)  SC: O(lognlognlogn)
def count_digit_sum_f(fromm, to):
    # f[i][sum][limited] = dict_sum(f[i+1][sum+digit][limited and digit == upper_bound] for digit in range(upper_bound+1))
    @cache
    def f(i, sum, limited, s):
        ans = defaultdict(int)
        if i == len(s):
            ans[sum] += 1
            return ans
        upper_bound = int(s[i]) if limited else 9
        for digit in range(upper_bound+1):
            tmp = f(i+1, sum+digit, limited and digit == upper_bound, s)
            for k in tmp:
                ans[k] += tmp[k]
        return ans
    
    d_to = f(0, 0, True, str(to))
    d_fromm = f(0, 0, True, str(fromm-1))
    for k in d_fromm:
        if k in d_to: 
            d_to[k] -= d_fromm[k]
            if d_to[k] <= 0: del d_to[k]
    return d_to

print(count_digit_sum_naive(34, 65782))
print(list(count_digit_sum_f(34, 65782).values())[:19])
