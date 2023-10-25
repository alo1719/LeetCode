#
# @lc app=leetcode.cn id=460 lang=python3
#
# [460] LFU Cache
#
# https://leetcode.cn/problems/lfu-cache/description/
#
# algorithms
# Hard (44.43%)
# Likes:    632
# Dislikes: 0
# Total Accepted:    60.4K
# Total Submissions: 135.9K
# Testcase Example:  '["LFUCache","put","put","get","put","get","get","put","get","get","get"]\n' +
  '[[2],[1,1],[2,2],[1],[3,3],[2],[3],[4,4],[1],[3],[4]]'
#
# Design and implement a data structure for a Least Frequently Used (LFU)
# cache.
# 
# Implement the LFUCache class:
# 
# 
# LFUCache(int capacity) Initializes the object with the capacity of the data
# structure.
# int get(int key) Gets the value of the key if the key exists in the cache.
# Otherwise, returns -1.
# void put(int key, int value) Update the value of the key if present, or
# inserts the key if not already present. When the cache reaches its capacity,
# it should invalidate and remove the least frequently used key before
# inserting a new item. For this problem, when there is a tie (i.e., two or
# more keys with the same frequency), the least recently used key would be
# invalidated.
# 
# 
# To determine the least frequently used key, a use counter is maintained for
# each key in the cache. The key with the smallest use counter is the least
# frequently used key.
# 
# When a key is first inserted into the cache, its use counter is set to 1 (due
# to the put operation). The use counter for a key in the cache is incremented
# either a get or put operation is called on it.
# 
# The functions get and put must each run in O(1) average time complexity.
# 
# 
# Example 1:
# 
# 
# Input
# ["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get",
# "get"]
# [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]]
# Output
# [null, null, null, 1, null, -1, 3, null, -1, 3, 4]
# 
# Explanation
# // cnt(x) = the use counter for key x
# // cache=[] will show the last used order for tiebreakers (leftmost element
# is  most recent)
# LFUCache lfu = new LFUCache(2);
# lfu.put(1, 1);   // cache=[1,_], cnt(1)=1
# lfu.put(2, 2);   // cache=[2,1], cnt(2)=1, cnt(1)=1
# lfu.get(1);      // return 1
# ⁠                // cache=[1,2], cnt(2)=1, cnt(1)=2
# lfu.put(3, 3);   // 2 is the LFU key because cnt(2)=1 is the smallest,
# invalidate 2.
# // cache=[3,1], cnt(3)=1, cnt(1)=2
# lfu.get(2);      // return -1 (not found)
# lfu.get(3);      // return 3
# ⁠                // cache=[3,1], cnt(3)=2, cnt(1)=2
# lfu.put(4, 4);   // Both 1 and 3 have the same cnt, but 1 is LRU, invalidate
# 1.
# ⁠                // cache=[4,3], cnt(4)=1, cnt(3)=2
# lfu.get(1);      // return -1 (not found)
# lfu.get(3);      // return 3
# ⁠                // cache=[3,4], cnt(4)=1, cnt(3)=3
# lfu.get(4);      // return 4
# ⁠                // cache=[4,3], cnt(4)=2, cnt(3)=3
# 
# 
# 
# Constraints:
# 
# 
# 1 <= capacity <= 10^4
# 0 <= key <= 10^5
# 0 <= value <= 10^9
# At most 2 * 10^5 calls will be made to get and put.
# 
# 
# 
# 
#

# @lc code=start
from collections import defaultdict


class Node:
    def __init__(self, key=-1, value=-1) -> None:
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        self.freq = 0

    def insert(self, node):
        node.prev = self
        node.next = self.next
        self.next.prev = node
        self.next = node

class LFUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0
        self.freq_dict = defaultdict(self.new_dll)
        self.key_dict = {} # key : node

    def get(self, key: int) -> int:
        if key in self.key_dict:
            self.add_freq(self.key_dict[key])
            return self.key_dict[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.key_dict:
            node = self.key_dict[key]
            node.value = value
        else:
            node = Node(key, value)
            self.key_dict[key] = node
            self.size += 1
        if self.size > self.capacity:
            self.size -= 1
            deleted_key = self.delete(self.freq_dict[self.min_freq][0].next)
            del self.key_dict[deleted_key]
        self.add_freq(node)

    def new_dll(self):
        head, tail = Node(), Node()
        head.next = tail
        tail.prev = head
        return (head, tail)
    
    def add_freq(self, node):
        if node.freq != 0: self.delete(node)
        node.freq += 1
        self.freq_dict[node.freq][1].prev.insert(node)
        if node.freq == 1:
            self.min_freq = 1
        elif self.min_freq == node.freq-1:
            if not self.freq_dict[self.min_freq][0].next.next: # no nodes
                self.min_freq = node.freq
    
    def delete(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        if node.prev == self.freq_dict[node.freq][0] and node.next == self.freq_dict[node.freq][1]:
            del self.freq_dict[node.freq]
        return node.key

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# @lc code=end

