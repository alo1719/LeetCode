from functools import *


def solution(nums):
    # f[i][+] = f[i-1][-] (nums[i] < 0), f[i-1][+] (nums[i] >= 0)
    # f[i][-] = f[i-1][+] (nums[i] <= 0), f[i-1][-] (nums[i] > 0)
    @cache
    def f(i, sign):
        if i == -1: return 0
        if sign == '+':
            if nums[i] < 0: return f(i-1, '-')
            else: return 1+f(i-1, '+')
        else:
            if nums[i] > 0: return f(i-1, '-')
            else: return 1+f(i-1, '+')
    n = len(nums)
    return sum(f(i, '-') for i in range(n)), sum(f(i, '+') for i in range(n))

print(solution([5,-3,3,-1,1]))  # 8, 7
print(solution([4,2,-4,3,1,2,-4,3,2,3]))  # 28, 27
print(solution([-1,-2,-3,-4,-5]))  # 9, 6