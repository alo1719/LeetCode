# 并查集
class UFDS:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.cnt = [1 for i in range(n)]
    
    def find(self, k):
        if self.root[k] == k:
            return k
        self.root[k] = self.find(self.root[k])
        return self.root[k]
    
    def union(self, a, b):
        x = self.find(a)
        y = self.find(b)
        if x != y:
            if self.cnt[x] > self.cnt[y]:
                x, y = y, x
            self.root[x] = y
            self.cnt[y] += self.cnt[x]
        return

def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    ufds = UFDS(n + 1)
    ans = []
    q = len(queryType)
    for i in range(q):
        query = queryType[i]
        student_1 = students1[i]
        student_2 = students2[i]
        if query == "Friend":
            ufds.union(student_1, student_2)
        if query == "Total":
            student_1_root = ufds.find(student_1)
            student_2_root = ufds.find(student_2)
            if student_1_root == student_2_root:
                ans.append(ufds.cnt[student_1_root])
            else:
                ans.append(ufds.cnt[student_1_root] + ufds.cnt[student_2_root])
    return ans