import bisect


def find_perfect_pairs(nums):
    for i in range(len(nums)):
        nums[i] = abs(nums[i])
    sorted_nums = sorted(nums)
    count = 0
    for i in range(len(sorted_nums)):
        curr = sorted_nums[i]
        right_index = bisect.bisect(sorted_nums, curr * 2) - 1
        if right_index > i:
            count += right_index - i
    return count
