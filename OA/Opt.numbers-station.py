d = {}
l = {}
r = {}

def numbers_station(num, ch):
    d[num] = ch
    flag = False
    if ch == '-' and num-1 in d:
        numbers_station(num-1, d[num-1])
        flag = True
    if ch == '-' and num+1 in d:
        numbers_station(num+1, d[num+1])
        flag = True
    if flag: return
    if num-1 in d and d[num-1] == '-': l[num] = num-1
    if num+1 in d and d[num+1] == '-': r[num] = num+1
    if num-1 in l:
        idx = num
        while idx in d and d[idx] != '-' and idx not in l:
            l[idx] = l[num-1]
            idx += 1
    if num+1 in r:
        idx = num
        while idx in d and d[idx] != '-' and idx not in r:
            r[idx] = r[num+1]
            idx -= 1
    if num in l:
        idx = num+1
        while idx in d and d[idx] != '-' and idx not in l:
            l[idx] = l[num]
            idx += 1
    if num in r:
        idx = num-1
        while idx in d and d[idx] != '-' and idx not in r:
            r[idx] = r[num]
            idx -= 1
    print(num, l, r)
    if num in l and num in r:
        print(''.join(d[i] for i in range(l[num]+1, r[num])))

# hello
# numbers_station(1, '-')
# numbers_station(2, 'h')
# numbers_station(3, 'e')
# numbers_station(4, 'l')
# numbers_station(5, 'l')
# numbers_station(6, 'o')
# numbers_station(7, '-')
# numbers_station(8, 'b')
# hi
# bye
# numbers_station(1, '-')
# numbers_station(2, 'b')
# numbers_station(3, 'y')
# numbers_station(5, '-')
# numbers_station(6, 'h')
# numbers_station(7, 'i')
# numbers_station(8, '-')
# numbers_station(4, 'e')
# a
# b
# numbers_station(1, '-')
# numbers_station(2, 'a')
# numbers_station(4, 'b')
# numbers_station(5, '-')
# numbers_station(3, '-')
# abc
# numbers_station(1, '-')
# numbers_station(5, '-')
# numbers_station(2, 'a')
# numbers_station(4, 'c')
# numbers_station(3, 'b')

