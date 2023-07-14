# Snowflake VOE
# Sliding window
# TC: O(n)  SC: O(n)
class Solution:
    def drop_request(self, arr):
        n, allowed, dropped = len(arr), [], []
        if not arr: return []
        left, last = 0, None
        for right in range(n):
            if not last or arr[right] != arr[last]: last = right
            if right-last >= 3:
                dropped.append(arr[right])
                continue
            while arr[right]-arr[left] >= 10: left += 1
            if len(allowed)-left+1 > 20:
                dropped.append(arr[right])
            else:
                allowed.append(arr[right])
        return dropped 
                

# rule 1: at most 3 requests per second
# rule 2: at most 20 requests per 10 seconds
print(Solution().drop_request([1,1,2,3,3,3]))  # []
print(Solution().drop_request([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,9,12,12,12]))  # [7,9]
print(Solution().drop_request([1,1,1,2,2,2,3,3,3,3]))  # [3]
print(Solution().drop_request([1,1,1,2,2,2,3,3,3,4,7,7,7,8,8,8,9,9,9,10,10,10,11,11,11]))  # [10,10]