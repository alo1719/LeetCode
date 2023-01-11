class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        ans=0
        def dfs(nums,now):
            nonlocal ans
            if not nums:
                ans+=1
                return
            for i in range(len(nums)):
                if nums[i] in nums[:i]:
                    continue
                if not now or math.sqrt(now[-1]+nums[i])%1==0:
                    dfs(nums[:i]+nums[i+1:],now+[nums[i]])
        dfs(nums,[])
        return ans