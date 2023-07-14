#
# @lc app=leetcode.cn id=146 lang=python3
#
# [146] LRU Cache
#
# https://leetcode.cn/problems/lru-cache/description/
#
# algorithms
# Medium (53.37%)
# Likes:    2452
# Dislikes: 0
# Total Accepted:    422.7K
# Total Submissions: 792K
# Testcase Example:  '["LRUCache","put","put","get","put","get","put","get","get","get"]\n' +
# '[[2],[1,1],[2,2],[1],[3,3],[2],[4,4],[1],[3],[4]]'
#
# Design a data structure that follows the constraints of a Least Recently Used
# (LRU) cache.
# 
# Implement the LRUCache class:
# 
# 
# LRUCache(int capacity) Initialize the LRU cache with positive size
# capacity.
# int get(int key) Return the value of the key if the key exists, otherwise
# return -1.
# void put(int key, int value) Update the value of the key if the key exists.
# Otherwise, add the key-value pair to the cache. If the number of keys exceeds
# the capacity from this operation, evict the least recently used key.
# 
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, null, -1, 3, 4]
# 
# Explanation
# LRUCache lRUCache = new LRUCache(2);
# lRUCache.put(1, 1); // cache is {1=1}
# lRUCache.put(2, 2); // cache is {1=1, 2=2}
# lRUCache.get(1);    // return 1
# lRUCache.put(3, 3); // LRU key was 2, evicts key 2, cache is {1=1, 3=3}
# lRUCache.get(2);    // returns -1 (not found)
# lRUCache.put(4, 4); // LRU key was 1, evicts key 1, cache is {4=4, 3=3}
# lRUCache.get(1);    // return -1 (not found)
# lRUCache.get(3);    // return 3
# lRUCache.get(4);    // return 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 3000
# 0 <= key <= 10^4
# 0 <= value <= 10^5
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
#

# @lc code=start
# K,V -> dict
# O(1) -> Doubly linked list
# Snowflake VOE
# LFU -> Another dict to store frequency
# freq dict: (freq, node), every freq has a doubly linked list, each node stores
# key, value and freq
# key dict: (key, mem address of the node)
class Node:
    def __init__(self, k=0, v=0):
        self.key = k
        self.value = v
        self.prev = None
        self.next = None

# TC: O(1)  SC: O(capacity)
class LRUCache:

    def __init__(self, capacity: int):
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cache = {}  # value : Node mem address
        self.capacity = capacity
        self.size = 0

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        else:
            node = self.cache[key]
            self.move2Head(node)  # 2B impl
            return node.value

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = Node(key, value)
            self.add2Head(node)  # 2B impl
            self.size += 1
            self.cache[key] = node
            if self.size > self.capacity:
                node = self.removeTail()  # 2B impl
                self.cache.pop(node.key)
                self.size -= 1
        else:
            node = self.cache[key]
            node.value = value
            self.move2Head(node)
    
    def move2Head(self, node):
        self.removeNode(node)  # 2B impl
        self.add2Head(node)
    
    # head <-> nodeXXX
    #     nodeWeWant2Add
    def add2Head(self, node):
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
    
    # node2BRemoved <-> tail
    def removeTail(self):
        return self.removeNode(self.tail.prev)
    
    # node1 <-> node <-> node2
    def removeNode(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

