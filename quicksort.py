def quick_sort(a):
    if len(a) <= 1:
        return a
    p = a[len(a) // 2]
    return quick_sort([x for x in a if x < p]) + [x for x in a if x == p] + quick_sort([x for x in a if x > p])


arr = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(quick_sort(arr))
