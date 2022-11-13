def validateSudoku(grid1):
    n = len(grid1[0])
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(grid1[i][j])
        for k in range(1, n+1):
            if k not in temp:
                return False
    for j in range(n):
        temp = []
        for i in range(n):
            temp.append(grid1[i][j])
        for k in range(1, n+1):
            if k not in temp:
                return False
    return True

print(validateSudoku([[1,2,3],[2,3,1],[3,1,2]]))