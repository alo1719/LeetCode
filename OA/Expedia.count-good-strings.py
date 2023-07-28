# TC: O(n)  SC: O(n)
def countGoodStrings(min_length, max_length, one_group, zero_group):
    # f[i] = f[i-one_group]+f[i-zero_group]
    f = [0]*(max_length+1)
    f[one_group] = 1
    f[zero_group] = 1
    for i in range(max(one_group, zero_group), max_length+1):
        f[i] += f[i-one_group] if i >= one_group else 0
        f[i] += f[i-zero_group] if i >= zero_group else 0
        f[i] %= 10**9+7
    return sum(f[min_length:max_length+1])%(10**9+7)


print(countGoodStrings(2, 7, 3, 2))  # 10