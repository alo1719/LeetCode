def max_array_val(nums):
    def can_achieve(nums, max_val):
        diff = 0
        for i in range(len(nums) - 1, -1, -1):
            diff = max(0, nums[i] + diff - max_val)
        return diff == 0
    
    low = nums[0]
    high = max(nums)
    while low < high:
        mid = (low + high) // 2
        if can_achieve(nums, mid):
            high = mid
        else:
            low = mid + 1
    return low

print(max_array_val([1, 5, 7, 6]))
print(max_array_val([5, 15, 19]))
print(max_array_val([10, 3, 5, 7]))
print(max_array_val([1, 8, 9, 1, 1]))