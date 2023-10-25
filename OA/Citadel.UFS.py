class UFS:
    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.cnt = [1 for _ in range(n)]
    
    def find(self, x):
        if self.root[x] == x: return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]
    
    def merge(self, a, b):
        root_a = self.find(a)
        root_b = self.find(b)
        self.root[root_a] = root_b
        self.cnt[root_b] += self.cnt[root_a]

# TC: O(n)  SC: O(n)
def getTheGroups(n, queryType, students1, students2):
    # Write your code here
    ufs = UFS(n+1)
    ans = []
    n = len(queryType)
    for i in range(n):
        query = queryType[i]
        student_1 = students1[i]
        student_2 = students2[i]
        if query == "Friend":
            ufs.merge(student_1, student_2)
        if query == "Total":
            student_1_root = ufs.find(student_1)
            student_2_root = ufs.find(student_2)
            if student_1_root == student_2_root:
                ans.append(ufs.cnt[student_1_root])
            else:
                ans.append(ufs.cnt[student_1_root]+ufs.cnt[student_2_root])
    return ans