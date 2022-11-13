# TC: O(n^2)
# SC: O(n^2)
def lcs(s1, s2):
    dp = [[0] * (len(s2)+1) for _ in range(len(s1)+1)]
    max = 0
    max_pos = -1
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
                if dp[i+1][j+1] > max:
                    max = dp[i+1][j+1]
                    max_pos = i+1
    print("[")
    print(",\n".join(s1[v] for v in range(max_pos-max,max_pos)))
    print("]")

s1 = ["3234.html", "xys.html", "7hsaa.html"]
s2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
lcs(s1,s2)