def compute_hash(s: str):
    p = 31
    m = 10**9+9
    p_pow = 1
    hash_value = 0
    for ch in s:
        hash_value = (hash_value + (ord(ch)-ord('a')+1) * p_pow) % m
        p_pow = (p_pow * p) % m
    return hash_value

# Notice that hash value can be manipulated like prefix sum!
def rabin_karp(string:str, pattern: str):
    p = 31
    m = 10**9+9
    patter_length, string_length = len(pattern), len(string)
    p_pow = [1] * max(patter_length, string_length)
    for i in range(1, len(p_pow)):
        p_pow[i] = (p_pow[i-1] * p) % m
    pattern_hash = [0] * patter_length
    string_hash = [0] * string_length
    for i in range(patter_length):
        last_hash_value = 0 if i == 0 else pattern_hash[i-1]
        pattern_hash[i] = (last_hash_value + (ord(pattern[i])-ord('a')+1) * p_pow[i]) % m
    for i in range(string_length):
        last_hash_value = 0 if i == 0 else string_hash[i-1]
        string_hash[i] = (last_hash_value + (ord(string[i])-ord('a')+1) * p_pow[i]) % m
    occurences = []
    for i in range(string_length-patter_length+1):
        last_hash_value = 0 if i == 0 else string_hash[i-1]
        cur_hash = (string_hash[i+patter_length-1] - last_hash_value + m) % m
        if (cur_hash == pattern_hash[patter_length-1] * p_pow[i] % m):
            occurences.append(i)
    return occurences

print(compute_hash("Xinyi Zhang"))
print(compute_hash("Xinyi Zhbng"))
print(rabin_karp("xinyi zhang", "xinyi"))
print(rabin_karp("acddaaderdaacfaaacdae", "aa"))