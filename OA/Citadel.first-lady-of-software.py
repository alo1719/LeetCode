# TC: O(1)  SC: O(1)
def first_lady_of_software(n_intervals, n_processes):  # <= 1000
    MOD = 10**9+7
    if n_processes == 1: return int(n_intervals == 1)
    return n_processes*((n_processes-1)**(n_intervals-1)%MOD)%MOD

print(first_lady_of_software(2, 1))  # 0
print(first_lady_of_software(2, 3))  # 6
