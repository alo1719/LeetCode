import bisect


# TC: O(n)  SC: O(1)
def find_perfect_pairs(nums):
    n = len(nums)
    for i in range(n):
        nums[i] = abs(nums[i])
    nums.sort()
    ans = 0
    right = -1
    for left in range(n):
        while right+1 < n and nums[right+1] <= 2*nums[left]:
            right += 1
        ans += right - left
    return ans

# A pair of integers (x,y) is perfect if both the below conditions are met:

# min(|x-y|,|x+y|)<=min(|x|,|y|)
# max(|x-y|,|x+y|)>=max(|x|,|y|)

# Given an array of length n, find the number of perfect pairs (arr[i], arr[j]) where 0<=i<j<n

# Exmaple:
# arr = [-9,6,-2,1] -> ans=2
# arr = [2,5,-3] -> ans = 2

# We need to understand the "physical" meaning of the two conditions.

# If x and y have the same sign, i.e., both positive or both negative, then:
# min(|x-y|,|x+y|)=|x-y|=||x|-|y|| (the difference between |x| and |y|)
# max(|x-y|,|x+y|)=|x+y|=|x|+|y|

# If x and y have different signs, i.e., one positive and one negative, then:
# min(|x-y|,|x+y|)=|x+y|=||x|-|y||
# max(|x-y|,|x+y|)=|x-y|=|x|+|y|

# So the two conditions mean:
# difference(|x|,|y|) <= min(|x|,|y|);
# |x|+|y|>=max(|x|,|y|), which is always true.

# If we sort the integers by their absolute values and suppose |x|<=|y|, then ||x|-|y||<=min(|x|,|y|) ==> |y|-|x|<=|x| ==> |y|<=2|x|
# The number of perfect pairs can be counted on the sorted arrays using two pointers with O(n) time complexity.
print(find_perfect_pairs([-9, 6, -2, 1]))
print(find_perfect_pairs([2, 5, -3]))