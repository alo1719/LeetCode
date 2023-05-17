# TC: O(n*m)
# SC: O(max(n,m))
def validateMonogram(matrix, rows, columns):
    m, n = len(rows), len(columns)
    for i in range(m):
        tmp, acc = [], 0
        for j in range(n):
            if matrix[i][j] == 'W':
                if acc == 0: continue
                else:
                    tmp.append(acc)
                    acc = 0
            else: acc += 1
        if acc != 0: tmp.append(acc)
        if str(rows[i]) != str(tmp): return False
    for j in range(n):
        tmp, acc = [], 0
        for i in range(m):
            if matrix[i][j] == 'W':
                if acc == 0: continue
                else:
                    tmp.append(acc)
                    acc = 0
            else: acc += 1
        if acc != 0: tmp.append(acc)
        if str(columns[j]) != str(tmp): return False
    return True

# count B in a row or column
matrix = [
['W','W','W','W'],
['B','W','W','W'],
['B','W','B','B'],
['W','W','B','W'],
['B','B','W','W']
]
rows = [[],[1],[1,2],[1],[2]]
columns = [[2,1],[1],[2],[1]]
print(validateMonogram(matrix, rows, columns))