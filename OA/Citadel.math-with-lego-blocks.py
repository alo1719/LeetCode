# TC: O(n)  SC: O(1)
def math_with_lego_blocks(a, b):  # n, m <= 100000, num <= 10000
    a0 = a.count(0)
    suma = sum(a)
    b0 = b.count(0)
    sumb = sum(b)
    if not a0 and not b0 and suma != sumb: return -1
    if not a0 and suma < sumb+b0: return -1
    if not b0 and sumb < suma+a0: return -1
    return max(suma+a0, sumb+b0)

print(math_with_lego_blocks([1,0,2],[1,3,0,0]))  # 6
print(math_with_lego_blocks([1,2],[1,3]))  # -1