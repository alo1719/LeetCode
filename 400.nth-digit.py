class Solution:
    def findNthDigit(self, n: int) -> int:
        def calcD(num):
            if num==0: return 0
            ans=0
            n=len(str(num))
            t=int("1"+(n-1)*"0")
            ans+=(num-t+1)*len(str(num))
            ans+=calcD(t-1)
            return ans
        l=1
        r=n
        while l<r:
            m=l+(r-l)//2
            # print(m, calcD(m))
            if (calcD(m)>=n):
                r=m
            else:
                l=m+1
        left=n-calcD(l-1)
        print(int(str(l)[left-1]))
        return int(str(l)[left-1])
