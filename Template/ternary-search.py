left, right = 0, n-1
while left < right:
    mid1 = (left+right)//2
    mid2 = (left+right)//2+1
    if arr[mid1] > arr[mid2]:
        right = mid1
    else:
        left = mid2
return left