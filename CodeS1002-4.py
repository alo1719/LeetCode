from typing import List


def solution(a:List[int]):
    d = {}
    for i,aa in enumerate(a):
        min = 9
        minpos = -1
        for minp,aaa in enumerate(str(aa)):
            if int(aaa) < min:
                min = int(aaa)
                minpos = minp
        print(minpos, min)
        front = str(aa)[:minpos]
        bd = str(aa)[minpos:] + front
        d.setdefault(bd, 0)
        d[bd]+=1
    ans = 0
    print(d)
    for a in d:
        print(a)
        if d[a] == 2: ans+=1
        if d[a] > 2: ans+=int(d[a]*(d[a]-1)/2)
    print(ans)
    return ans


solution([1,1,1,1])
print(solution([13, 5604,31,2,13,4560,546,654,456]))