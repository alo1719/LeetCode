class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        m={}
        l=[]
        r={}
        for i in range(0,len(equations)):
            fst=equations[i][0]
            sec=equations[i][1]
            if fst not in m:
                m[fst]={}
                r[fst]={}
                l.append(fst)
            if sec not in m:
                m[sec]={}
                r[sec]={}
                l.append(sec)
            m[fst][sec]=values[i]
            m[sec][fst]=1/values[i]
            r[fst][sec]=[fst,sec]
            r[sec][fst]=[sec,fst]
        print(m)
        print(l)
        for k in l:
            for i in l:
                for j in l:
                    if j not in m[i] and (k in m[i] and j in m[k]):
                        m[i][j]=m[i][k]*m[k][j]
                        r[i][j]=r[i][k]+r[k][j]
        print(m)
        ans=[]
        ans2=[]
        for q in queries:
            fst=q[0]
            sec=q[1]
            if fst in m and sec in m and sec in m[fst]:
                ans.append(m[fst][sec])
                ans2.append(r[fst][sec])
            else:
                ans.append(-1)
                ans2.append("Not Possible")
        print(ans2)
        return ans