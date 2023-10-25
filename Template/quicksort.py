# Snowflake VOE
# TC: O(nlogn)  SC: O(n)
def quick_sort_not_in_place(a):
    if len(a) <= 1:
        return a
    p = a[len(a)//2]
    return quick_sort_not_in_place([x for x in a if x < p])+[x for x in a if x == p]+quick_sort_not_in_place([x for x in a if x > p])

# TC: O(nlogn)  SC: O(logn)
def quick_sort(a, begin, end):
    if begin >= end: return
    pivot = partition(a, begin, end)
    quick_sort(a, begin, pivot-1)
    quick_sort(a, pivot+1, end)

# TC: O(n)  SC: O(1)
def partition(a, begin, end):
    pivot = (begin+end)//2
    a[begin], a[pivot] = a[pivot], a[begin]  # pivot swap to begin to simplify
    pivot = begin
    for i in range(begin+1, end+1):
        if a[i] < a[begin]:
            pivot += 1
            a[i], a[pivot] = a[pivot], a[i]
    a[pivot], a[begin] = a[begin], a[pivot]
    return pivot

# TC: O(n)  SC: O(logn)
def find_no_k(a, begin, end, k):
    pivot = partition(a, begin, end)
    if pivot > k:
        return find_no_k(a, begin, pivot-1, k)
    elif pivot < k:
        return find_no_k(a, pivot+1, end, k)
    else:
        return a[pivot]

# TC: O(n)  SC: O(logn)
def find_median(a):
    if len(a)%2 == 1:
        return find_no_k(a, 0, len(a)-1, len(a)//2)
    else:
        return (find_no_k(a, 0, len(a)-1, len(a)//2-1)+find_no_k(a, 0, len(a)-1, len(a)//2))/2

arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
arr2 = [54, 26, 93, 17, 77, 31, 44, 55, 20, 31, 44]
print(quick_sort_not_in_place(arr))
print(find_median(arr))
print(find_median(arr2))
quick_sort(arr, 0, len(arr)-1)
quick_sort(arr2, 0, len(arr2)-1)
print(arr)
print(arr2)
