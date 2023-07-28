# TC: O(n^2)
# SC: O(n)
def lcs(s1, s2):
    # f[i][j] = f[i-1][j-1]+1 if s1[i] == s2[j] else max(f[i-1][j], f[i][j-1])
    # f: longest length of s1[:i] and s2[:j]
    f = [[0]*(len(s2)+1) for _ in range(2)]
    maxx = 0
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                f[i%2][j] = f[(i+1)%2][j-1]+1
                if f[i%2][j] > maxx:
                    maxx = f[i%2][j]
            else:
                f[i%2][j] = max(f[i%2][j-1], f[(i+1)%2][j])
    print("[")
    for j in range(1, len(s2)+1):
        if f[len(s1)%2][j]-f[len(s1)%2][j-1]: print(s2[j-1], end=",\n")
    print("]")

s1 = ["3234.html", "xys.html", "123.html", "7hsaa.html"]
s2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
# [
# 3234.html,
# xys.html,
# 7hsaa.html,
# ]
lcs(s1, s2)