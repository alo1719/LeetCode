# TC: O(nlogm)  SC: O(1)  m is the max value of arr
def calc_threshold(arr, threshold):

    low, high, n = 0, max(arr), len(arr)
    while low < high:
        mid = (low+high)//2+1
        sum = 0
        for i in range(n):
            sum += max(0, arr[i]-mid)
        if sum >= threshold:
            low = mid
        else:
            high = mid-1
    return high

initialEnergy = [4,8,7,1,2]
print(calc_threshold(initialEnergy, 9))
initialEnergy = [5,2,13,10,8]
print(calc_threshold(initialEnergy, 8))