from collections import defaultdict


def function(matrix):
    n = len(matrix)
    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for i in matrix:
        for j in i:
            d1[j] += 1
    p = n-1
    for i in range(n//2):
        d2[matrix[i][i]] += 1
        d2[matrix[i][p]] += 1
        p-=1
    for i in range(n//2,n):
        d2[matrix[i][n//2]] += 1
    d1[0]-=d2[0]
    d1[1]-=d2[1]
    d1[2]-=d2[2]
    t1=d2[1]+d2[2]-min(d1[0]+d1[1], d1[0]+d1[2])
    t2=d2[0]+d2[2]-min(d1[1]+d1[2], d1[0]+d1[1])
    t3=d2[1]+d2[0]-min(d1[0]+d1[2], d1[1]+d1[2])
    return min(t1,t2,t3)