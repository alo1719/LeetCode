# Expedia OA1
def getSmallestArray(arr, l, r):
    brr = [l] * len(arr)

    for i in range(1, len(arr)):
        brr[i] = brr[i-1] - arr[i-1] + arr[i] + 1
        if brr[i] < brr[i-1]: brr[i] = brr[i-1]
        if brr[i] > r: return [-1]

    return brr


print(getSmallestArray([1,2,1,2], 1, 10))
print(getSmallestArray([1,2,1,3], 1, 10))
print(getSmallestArray([1,2,1,3], 1, 5))