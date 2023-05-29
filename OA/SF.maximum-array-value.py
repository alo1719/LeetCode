# TC: O(nlogn)  SC: O(1)
def max_array_val(nums):
    def can_achieve(nums, max_val):
        overflow = 0
        for i in range(len(nums)-1, -1, -1):
            overflow = max(0, nums[i] + overflow - max_val)
        return overflow == 0
    
    low = nums[0]
    high = max(nums)
    while low < high:
        mid = (low + high) // 2
        if can_achieve(nums, mid):
            high = mid
        else:
            low = mid + 1
    return low

# can only move leftwards
print(max_array_val([1, 5, 7, 6])) # 5
print(max_array_val([5, 15, 19])) # 13
print(max_array_val([10, 3, 5, 7])) # 10
print(max_array_val([1, 8, 9, 1, 1])) # 6