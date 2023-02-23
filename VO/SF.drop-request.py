# Snowflake VOE
# Sliding window
class Solution:
    def drop_request(self, a):
        n = len(a)
        a_allow = []
        a_drop = []
        if not a:
            return a
        left, right, right_beginning = 0, 0, 0
        a_allow.append(a[0])
        while left < len(a_allow):
            while right+1 < n and a[right+1]-a_allow[left]<=9:
                right += 1
                if a[right] != a[right_beginning]:
                    right_beginning = right
                if right - right_beginning > 2:
                    a_drop.append(a[right]) # rule 1
                else: # rule 2
                    right_in_allow = len(a_allow)-1
                    if right_in_allow - left >= 19:
                        a_drop.append(a[right])
                    else:
                        a_allow.append(a[right])
            left += 1
        print(a_allow)
        print(a_drop)
        return a_drop

Solution().drop_request([1,1,2,3,3,3]) # []
Solution().drop_request([1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,9,12,12,12]) # [7,9]
Solution().drop_request([1,1,1,2,2,2,3,3,3,3]) # [3]