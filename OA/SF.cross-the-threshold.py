import bisect


def calc_threshold(a, th):

    low, high = 0, max(a)
    while low < high:
        mid = (low + high) // 2 + 1
        print("mid: ", mid)
        sum = 0
        for i in range(len(a)):
            sum += max(0, a[i] - mid)
        print("sum: ", sum)
        if sum >= th:
            low = mid
        else:
            high = mid - 1
    print(high)
    return high

initialEnergy = [4,8,7,1,2]
calc_threshold(initialEnergy, 9)
initialEnergy = [5,2,13,10,8]
calc_threshold(initialEnergy, 8)