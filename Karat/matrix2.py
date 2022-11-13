# SC: O(max(n,m))
# TC: O(n*m)
def validateNonogram(matrix, rows, columns):
    n = len(rows)
    m = len(columns)
    for i in range(n):
        acc = 0
        temp = []
        for j in range(m):
            if matrix[i][j] == 'W':
                if acc == 0:
                    continue
                else:
                    temp.append(acc)
                    acc = 0
            if matrix[i][j] == 'B':
                acc += 1
        if acc != 0: temp.append(acc)
        if len(rows[i]) != len(temp): return False
        for k in range(len(temp)):
            if rows[i][k] != temp[k]: return False
    for j in range(m):
        acc = 0
        temp = []
        for i in range(n):
            if matrix[i][j] == 'W':
                if acc == 0:
                    continue
                else:
                    temp.append(acc)
                    acc = 0
            if matrix[i][j] == 'B':
                acc += 1
        if acc != 0: temp.append(acc)
        if len(columns[j]) != len(temp): return False
        for k in range(len(temp)):
            if columns[j][k] != temp[k]: return False
    return True

matrix1 = [
	['W','W','W','W'],
	['B','W','W','W'],
	['B','W','B','B'],
	['W','W','B','W'],
	['B','B','W','W']
]
rows1_1 = [[],[1],[1,2],[1],[2]]
columns1_1 = [[2,1],[1],[2],[1]]
print(validateNonogram(matrix1, rows1_1, columns1_1))