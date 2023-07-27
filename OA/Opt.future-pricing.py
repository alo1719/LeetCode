# DIVIDEND_UPDATE(i, A, D)  A: Amount, D: Day, operations <= 500
# PRICE(F)->output day F based on N dividends, operation <= 10^5
# Q operations
# 1 <= N, Q <= 10^5
# 1 <= S, A <= 10^9
# 1 <= D, F <= 10^6
from math import inf
from bisect import bisect_right


def future_pricing(S, N, Q, dividends, operations):
#                             A, D     P(F)/D(i,A,D)
    p = [(0, S)]
    sorted_dividends = sorted(dividends, key=lambda x:x[1])
    acc = S
    for A, D in sorted_dividends:
        acc -= A
        p.append((D, acc))
    ans = []
    for q in operations:
        if q[0] == 'PRICE':
            day = q[1]
            idx = bisect_right(p, (day, inf))-1
            ans.append(p[idx][1])
        else:
            i, A, D = q[1:]
            old_A, old_day = dividends[i-1]
            idx = bisect_right(p, (old_day, inf))-1
            for j in range(idx+1, len(p)):
                p[j] = (p[j][0], p[j][1]+old_A)
            del p[idx]
            idx = bisect_right(p, (D, inf))
            for j in range(idx, len(p)):
                p[j] = (p[j][0], p[j][1]-A)
            p.insert(idx, (D, p[idx-1][1]-A))
    return ans

print(future_pricing(1000, 2, 4, [(100, 10), (50, 100)], [['PRICE',15],['DIVIDEND_UPDATE',2,40,20],['PRICE',15],['PRICE',25]]))  # 900, 900, 860
print(future_pricing(1000, 2, 4, [(100, 10), (50, 100)], [['PRICE',15],['DIVIDEND_UPDATE',1,40,20],['PRICE',15],['PRICE',25]]))  # 900, 1000, 960