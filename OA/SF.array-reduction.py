from collections import defaultdict


def get_mex(a, i, j):
    mex = 0
    seen = set()
    for k in range(i, j+1):
        seen.add(a[k])
        while mex in seen:
            mex += 1
    return mex

# TC: O(n)  SC: O(n)
def mex_reduction(a):
    n = len(a)
    # mex is the highest mex possible for any suffix of a
    # at any given time, initially the suffix is the whole array
    mex = get_mex(a, 0, n-1)
    # count of elements in the suffix we're dealing with
    cnt = defaultdict(int)
    for el in a:
        cnt[el] += 1
    ans = []

    i = 0
    while i < n:
        cur_mex = 0
        seen = set()
        # the only way to get the lexicographically maximum
        # array is to always take the highest mex possible,
        # so we will do that and stop as soon as we have it
        while cur_mex != mex:
            el = a[i]
            cnt[el] -= 1
            seen.add(el)

            while cur_mex in seen:
                cur_mex += 1
            i += 1
        ans.append(cur_mex)
        
        # if curMex is 0, we need to take at least one element
        if cur_mex == 0:
            i += 1

        # next mex must be less than or equal to curMex,
        # and curMex <= the number of elements we just iterated
        # so this part of the code is O(N) worst case, BUT
        # it's also O(N) amortized over the whole call even
        # in the worst case, so overall TC is still O(N).
        next_mex = 0
        while cnt[next_mex] > 0:
            next_mex += 1
        mex = next_mex

    return ans


print(mex_reduction([0,1,1,0]))
print(mex_reduction([2,2,3,4,0,1,2,0]))