# TC: O(nlogn)  SC: O(n)
# [a, b, c]  [d, e, f]
#  i          j
# [a, b, c, d, e, f]
#  k
def merge_sort(arr):
    n = len(arr)
    ans = [0] * n
    seg = 1
    while seg < n:
        for start in range(0, n, seg*2):
            mid = min(start+seg, n)
            end = min(start+seg*2, n)
            k = i = start
            j = mid
            while i < mid or j < end:
                if j == end or (i < mid and arr[i] < arr[j]):
                    ans[k] = arr[i]
                    i += 1
                    k += 1
                else:
                    ans[k] = arr[j]
                    j += 1
                    k += 1
        seg *= 2
        arr, ans = ans, arr
    return arr # not ans because it has been swapped

arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(merge_sort(arr))
