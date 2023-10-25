#
# @lc app=leetcode.cn id=706 lang=python3
#
# [706] Design HashMap
#
# https://leetcode.cn/problems/design-hashmap/description/
#
# algorithms
# Easy (63.72%)
# Likes:    362
# Dislikes: 0
# Total Accepted:    95.6K
# Total Submissions: 150.3K
# Testcase Example:  '["MyHashMap","put","put","get","get","put","get","remove","get"]\n' +
  '[[],[1,1],[2,2],[1],[3],[2,1],[2],[2],[2]]'
#
# Design a HashMap without using any built-in hash table libraries.
# 
# Implement the MyHashMap class:
# 
# 
# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If
# the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or
# -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map
# contains the mapping for the key.
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]
# Output
# [null, null, null, 1, -1, null, 1, null, -1]
# 
# Explanation
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1);    // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3);    // return -1 (i.e., not found), The map is now [[1,1],
# [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the
# existing value)
# myHashMap.get(2);    // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2);    // return -1 (i.e., not found), The map is now
# [[1,1]]
# 
# 
# 
# Constraints:
# 
# 
# 0 <= key, value <= 10^6
# At most 10^4 calls will be made to put, get, and remove.
# 
# 
#

# @lc code=start
from collections import deque


class MyHashMap:

    def __init__(self):
        self.bucket_num = 10009
        self.map = [None]*self.bucket_num

    def put(self, key: int, value: int) -> None:
        hash = key%self.bucket_num
        if not self.map[hash]:
            self.map[hash] = deque()
        for item in self.map[hash]:
            if item[0] == key:
                item[1] = value
                return
        self.map[hash].append([key, value])

    def get(self, key: int) -> int:
        hash = key%self.bucket_num
        if not self.map[hash]: return -1
        for item in self.map[hash]:
            if item[0] == key:
                return item[1]
        return -1

    def remove(self, key: int) -> None:
        hash = key%self.bucket_num
        if not self.map[hash]: return
        for item in self.map[hash]:
            if item[0] == key:
                self.map[hash].remove(item)
                return



# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
# @lc code=end

