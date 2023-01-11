class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        sum = 0
        for num in nums:
            sum += num
        goal = sum - x
        n = len(nums)
        now = 0
        ans = -1
        l = 0
        for r in range(n):
            now += nums[r]
            while (now > goal and l < n):
                now -= nums[l]
                l += 1
            if now == goal:
                ans = max(ans, r - l + 1)
        return n - ans if ans != -1 else -1
