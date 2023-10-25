#
# @lc app=leetcode.cn id=981 lang=python3
#
# [981] Time Based Key-Value Store
#
# https://leetcode.cn/problems/time-based-key-value-store/description/
#
# algorithms
# Medium (53.10%)
# Likes:    198
# Dislikes: 0
# Total Accepted:    29K
# Total Submissions: 54.7K
# Testcase Example:  '["TimeMap","set","get","get","set","get","get"]\n' +
# '[[],["foo","bar",1],["foo",1],["foo",3],["foo","bar2",4],["foo",4],["foo",5]]'
#
# Design a time-based key-value data structure that can store multiple values
# for the same key at different time stamps and retrieve the key's value at a
# certain timestamp.
# 
# Implement the TimeMap class:
# 
# 
# TimeMap() Initializes the object of the data structure.
# void set(String key, String value, int timestamp) Stores the key key with the
# value value at the given time timestamp.
# String get(String key, int timestamp) Returns a value such that set was
# called previously, with timestamp_prev <= timestamp. If there are multiple
# such values, it returns the value associated with the largest timestamp_prev.
# If there are no values, it returns "".
# 
# 
# 
# Example 1:
# 
# 
# Input
# ["TimeMap", "set", "get", "get", "set", "get", "get"]
# [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo",
# 4], ["foo", 5]]
# Output
# [null, null, "bar", "bar", null, "bar2", "bar2"]
# 
# Explanation
# TimeMap timeMap = new TimeMap();
# timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along
# with timestamp = 1.
# timeMap.get("foo", 1);         // return "bar"
# timeMap.get("foo", 3);         // return "bar", since there is no value
# corresponding to foo at timestamp 3 and timestamp 2, then the only value is
# at timestamp 1 is "bar".
# timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along
# with timestamp = 4.
# timeMap.get("foo", 4);         // return "bar2"
# timeMap.get("foo", 5);         // return "bar2"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= key.length, value.length <= 100
# key and value consist of lowercase English letters and digits.
# 1 <= timestamp <= 10^7
# All the timestamps timestamp of set are strictly increasing.
# At most 2 * 10^5 calls will be made to set and get.
# 
# 
#

# @lc code=start
# Snowflake VOE
from collections import defaultdict


class TimeMap:

    def __init__(self):
        self.dict = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or timestamp < self.dict[key][0][0]:
            return ""
        left, right = 0, len(self.dict[key])-1
        while left < right:
            mid = (left + right + 1) // 2
            if self.dict[key][mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1

        return self.dict[key][left][1]
      
class TimeMapSF:

    def __init__(self):
        self.dict = defaultdict(list)
        self.temp = {}

    def set(self, key: str, value: str) -> None:
        self.temp[key] = value

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict or timestamp < self.dict[key][0][0]:
            return "null"
        left, right = 0, len(self.dict[key])-1
        while left < right:
            mid = (left + right + 1) // 2
            if self.dict[key][mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1
        return self.dict[key][left][1]

    def commit(self, key: str, timestamp: str) -> None:
        if key in self.temp:
            self.dict[key].append((timestamp, self.temp[key]))


kv = TimeMapSF()
print(kv.get("1", 1))
kv.set("1", 1)
print(kv.get("1", 1))
kv.commit("1", 2)
print(kv.get("1", 1))
print(kv.get("1", 2))
kv.set("1", -1)
kv.commit("1", 4)
print(kv.get("1", 3))
print(kv.get("1", 4))
print(kv.get("1", 5))








# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
# @lc code=end

