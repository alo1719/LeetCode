# TC: O(n^2)
# SC: O(n)
def lcs(s1, s2):
    # when use rolling array, need to consider "dirty" dp value
    # but since j is from [0, len(s2)-1], so in this case it is fine
    dp = [[0]*(len(s2)+1) for _ in range(2)]
    max = 0
    max_pos = -1
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                dp[(i+1)%2][j+1] = dp[i%2][j]+1
                if dp[(i+1)%2][j+1] > max:
                    max = dp[(i+1)%2][j+1]
                    max_pos = i+1
    print("[")
    print(",\n".join(s1[v] for v in range(max_pos-max, max_pos)))
    print("]")

s1 = ["3234.html", "xys.html", "7hsaa.html"]
s2 = ["3234.html", "sdhsfjdsh.html", "xys.html", "7hsaa.html"]
lcs(s1, s2)