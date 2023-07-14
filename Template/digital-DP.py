# mask: already used digits
# limited: whether the current digit is limited (number cannot be larger than maximum)
# valid: if current number is a number (not all leading 0s)
# mask can be replaced by sum, valid may not be needed
@cache
def f(i, mask, limited, valid):
    if i == len(s): return int(valid)
    ans = 0
    if not valid:
        ans = f(i+1, mask, False, False)
    upper_bound = int(s[i]) if limited else 9
    for digit in range(1-int(valid), upper_bound+1):
        if mask>>digit&1 == 0:
            ans += f(i+1, mask|(1<<digit), limited and digit==upper_bound, True)
    return ans

f(0, 0, True, False)