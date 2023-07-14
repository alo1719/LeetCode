from functools import *

# f(i, j): number i, partitioned into j groups, ways
# first put 1 into each group, then we have i-j left to put into at most j groups:
# f(i, j) = f(i-j, 1)+f(i-j, 2)+...+f(i-j, j-1)+f(i-j, j)
# note that f(i-1, j-1) = f(i-j, 1)+f(i-j, 2)+...+f(i-j, j-1)
# so f(i, j) = f(i-1, j-1)+f(i-j, j)
# can also be seen as "contain at least one 1" and "contain no 1 (2 at least)"
# f(_, 1) = 1, i >= j
# TC: O(nk)  SC: O(nk)
def grouping_options(n: int, k: int):  # 1 <= n,k <= 200
    @cache
    def f(i, j):
        if i < j: return 0
        if j == 1: return 1
        return f(i-1, j-1)+f(i-j, j)
    return f(n, k)


print(grouping_options(4, 2))  # 2
print(grouping_options(8, 4))  # 5
print(grouping_options(7, 3))  # 4
print(grouping_options(24, 5))  # 164
print(grouping_options(24, 5))  # 164
print(grouping_options(4, 5))  # 0
