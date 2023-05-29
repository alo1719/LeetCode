import bisect

# TC: O(nm lognm)  SC: O(nm)
def server_selection(servers):
    def check_possible(vul):
        cols, flag = set(), False
        for row in servers_sorted:
            index = bisect.bisect_left(row, (vul,))
            for i in range(index, m):
                if row[i][1] not in cols:
                    cols.add(row[i][1])
                flag |= index < (m-1) # m-1 rows: at least one row has two valid servers
                if len(cols) == m and flag:
                    return True
        return False
    
    m = len(servers[0])
    # each row: (vul, col_index)
    servers_sorted = [sorted((vul, i) for i, vul in enumerate(row)) for row in servers]
    nums = sorted({i for row in servers for i in row})
    
    low, high = 0, len(nums)-1
    while low < high:
        mid = (low + high + 1) // 2
        if check_possible(nums[mid]):
            low = mid
        else:
            high = mid - 1
    return nums[low]


# The developers of Hackerland want to build a distributed system. It is
# represented as a grid of n rows and m columns where n>=m and each
# cell is a server. The vulnerabllity of the ith-server in the jth-column is
# vulnerability[i][j]
# The net vulnerability of a system is the minimum vulnerability of
# the maximum vulnerabilities of the servers in all the columns. In
# other words, create a set of maximum vulnerabilites from each
# column of the grid and find the minimum of this set.
# They want to consider only a subset of m rows to increase net
# vulnerability. Find the maximum possible value of net vulnerablllty
# that can be achieved by choosing exactly m-1 rows from the grid.
servers = [[1,3,1],[3,1,1],[1,2,2],[1,1,3]]
print(server_selection(servers)) # 2
servers = [[5,3,3],[3,4,6],[2,4,1],[2,1,6]]
print(server_selection(servers)) # 4