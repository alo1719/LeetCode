from collections import defaultdict

# Snowflake VOE
# TC: O(n)  SC: O(n)
def loop_calc(arr):
    pos, ans = [0, 0], float("inf")
    pos_dict = defaultdict(int)
    for i, direction in enumerate(arr):
        if direction == "R":
            pos[0] += 1
        elif direction =="L":
            pos[0] -= 1
        elif direction == "U":
            pos[1] += 1
        elif direction == "D":
            pos[1] -= 1
        if (pos[0], pos[1]) in pos_dict:
            ans = min(ans, i-pos_dict[(pos[0], pos[1])])
        pos_dict[(pos[0], pos[1])] = i
    return ans

print(loop_calc(["R","R","R","U","L","D","D"])) # 4
print(loop_calc(["R","R","R","L","U","L","D","D"])) # 2
