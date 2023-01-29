import bisect


def server_selection(servers):
    n, m = len(servers), len(servers[0])
    servers_sorted = [sorted((vul, i) for i, vul in enumerate(row)) for row in servers]
    print(servers_sorted)
    nums = sorted({i for row in servers for i in row})
    print(nums)
    
    def check_possible(vul):
        print("vul:", vul)
        cols, flag = set(), 0
        for row in servers_sorted:
            index = bisect.bisect_left(row, (vul,))
            print("index:", index)
            for i in range(index, m):
                if row[i][1] not in cols:
                    print("cols.add:", row[i][1])
                    cols.add(row[i][1])
                print("flag |= :", index < (m - 1))
                flag |= index < (m - 1) # at most m - 1 rows
                if len(cols) == m and flag:
                    print("return True")
                    return True
        print("return False")
        return False
    
    low, high = 0, len(nums) - 1
    while low < high:
        mid = (low + high + 1) // 2
        if check_possible(nums[mid]):
            low = mid
        else:
            high = mid - 1
    print(nums[low])
    return nums[low]

servers = [[1,3,1],[3,1,1],[1,2,2],[1,1,3]]
server_selection(servers)
# servers = [[5,3,3],[3,4,6],[2,4,1],[2,1,6]]
# server_selection(servers)