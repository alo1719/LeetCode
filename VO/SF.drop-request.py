# Snowflake VOE
# Sliding window
# TC: O(n)  SC: O(n)
class Solution:
    def drop_request(self, arr):
        n, allowed, dropped = len(arr), [], []
        if not arr: return arr
        left, right, first = 0, 0, 0
        allowed.append(arr[0])
        while left < len(allowed):
            while right+1 < n and arr[right+1]-allowed[left] <= 9:
                right += 1
                if arr[right] != arr[first]: first = right
                if right-first > 2:
                    dropped.append(arr[right])  # rule 1
                else:  # rule 2
                    if len(allowed)-left >= 20:
                        dropped.append(arr[right])
                    else:
                        allowed.append(arr[right])
            left += 1
        return dropped

# rule 1: at most 3 requests per second
# rule 2: at most 20 requests per 10 seconds
print(Solution().drop_request([1,1,2,3,3,3]))  # []
print(Solution().drop_request([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,9,12,12,12]))  # [7,9]
print(Solution().drop_request([1,1,1,2,2,2,3,3,3,3]))  # [3]