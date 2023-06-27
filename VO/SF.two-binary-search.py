# Snowflake VOE
# TC: O(logn)  SC: O(1)
def two_binary_search(arr, a, b): # [a,b)
    if not arr or b <= arr[0] or a > arr[-1]: return 0
    # 1. find the left most element that >= a
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right)//2
        if arr[mid] >= a:
            right = mid
        else:
            left = mid+1
    pos_a = left
    # 2. find the right most element that < b
    left, right = 0, len(arr)-1
    while left < right:
        mid = (left+right+1)//2
        if arr[mid] < b:
            left = mid
        else:
            right = mid-1
    pos_b = left
    return pos_b-pos_a+1

print(two_binary_search([3,5,6,6,8,9,12,59], 5, 9))  # 4
print(two_binary_search([3,5,6,6,8,9,12,59], 4, 9))  # 4
print(two_binary_search([3,5,6,6,8,9,12,59], 4, 13))  # 6
print(two_binary_search([3,5,6,6,8,9,12,59], 1, 2))  # 0
print(two_binary_search([3,5,6,6,8,9,12,59], 65, 68))  # 0
print(two_binary_search([3,5,6,6,8,9,12,59], 10, 59))  # 1
print(two_binary_search([3,5,6,6,8,9,12,59], 10, 60))  # 2