class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        a=[0]*10002
        max=0
        ans=[]
        tmp=[]
        for itv in intervals:
            b=itv[0]
            e=itv[1]
            if e>max: max=e
            if b==e: tmp.append([b,e])
            for i in range(b,e):
                a[i]=1
        for tmpi in tmp:
            b=tmpi[0]
            if b==0 and a[b]==0 and [b,b] not in ans: ans.append([b,b])
            if b!=0 and a[b]==0 and a[b-1]==0 and [b,b] not in ans: ans.append([b,b])
        inrange=False
        for i in range(0,max+2):
            if a[i]==1 and not inrange:
                b=i
            if a[i]==0 and inrange:
                e=i
                ans.append([b,e])
            if a[i]==1: inrange=True
            else: inrange=False
        print(ans)
        return ans