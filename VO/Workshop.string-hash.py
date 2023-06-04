# TC: O(len(s))  SC: O(1), TC can be seen as O(1)
def compute_hash(s: str):
    prime = 31
    mod = 10**9+9
    pow = 1
    hash_value = 0
    for ch in s:
        hash_value = (hash_value + (ord(ch)-ord('a')+1) * pow) % mod
        pow = (pow * prime) % mod
    return hash_value

# Notice that hash value can be manipulated like prefix sum!
# TC: O(n)  SC: O(n)
def rabin_karp(string: str, pattern: str):
    prime = 31
    mod = 10**9+9
    patter_len, string_len = len(pattern), len(string)
    pow = [1] * max(patter_len, string_len)
    for i in range(1, len(pow)):
        pow[i] = (pow[i-1] * prime) % mod
    pattern_hash = 0
    string_hash = [0] * string_len
    for i in range(patter_len):
        pattern_hash = (pattern_hash + (ord(pattern[i])-ord('a')+1) * pow[i]) % mod
    for i in range(string_len):
        last_hash_value = 0 if i == 0 else string_hash[i-1]
        string_hash[i] = (last_hash_value + (ord(string[i])-ord('a')+1) * pow[i]) % mod
    occurences = []
    for i in range(string_len-patter_len+1):
        last_hash_value = 0 if i == 0 else string_hash[i-1]
        # hash of [i, j] is (hash[j] - hash[i-1])
        cur_hash = (string_hash[i+patter_len-1] - last_hash_value + mod) % mod
        # shift pattern hash
        if (cur_hash == pattern_hash * pow[i] % mod):
            occurences.append(i)
    return occurences

print(compute_hash("Xinyi Zhang")) # 507870207
print(compute_hash("Xinyi Zhbng")) # 398899971
print(rabin_karp("xinyi zhang", "xinyi")) # [0]
print(rabin_karp("acddaaderdaacfaaacdae", "aa")) # [4, 10, 14, 15]