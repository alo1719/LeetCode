# We can shift a string by shifting each of its letters to its successive letter.

# For example, "abc" can be shifted to be "bcd".
# We can keep shifting the string to form a sequence.

# For example, we can keep shifting "abc" to form the sequence: "abc" -> "bcd" -> ... -> "xyz".
# Given an array of strings strings, group all strings[i] that belong to the same shifting sequence. You may return the answer in any order.

#  

# Example 1:

# Input: strings = ["abc","bcd","acef","xyz","az","ba","a","z"]
# Output: [["acef"],["a","z"],["abc","bcd","xyz"],["az","ba"]]
# Example 2:

# Input: strings = ["a"]
# Output: [["a"]]
#  

# Constraints:

# 1 <= strings.length <= 200
# 1 <= strings[i].length <= 50
# strings[i] consists of lowercase English letters.
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dist_dict = {}
        for s in strings:
            dist = tuple([(26 + ord(c) - ord(s[0])) % 26 for c in s])
            dist_dict.setdefault(dist, []).append(s)
        # print(dist_dict)
        # print(list(dist_dict.values()))
        return list(dist_dict.values())


Solution().groupStrings(["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"])
Solution().groupStrings(["a"])
