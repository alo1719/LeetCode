#
# @lc app=leetcode id=692 lang=python3
#
# [692] Top K Frequent Words
#
# https://leetcode.com/problems/top-k-frequent-words/description/
#
# algorithms
# Medium (57.47%)
# Likes:    7358
# Dislikes: 336
# Total Accepted:    572.9K
# Total Submissions: 996.2K
# Testcase Example:  '["i","love","leetcode","i","love","coding"]\n2'
#
# Given an array of strings words and an integer k, return the k most frequent
# strings.
# 
# Return the answer sorted by the frequency from highest to lowest. Sort the
# words with the same frequency by their lexicographical order.
# 
# 
# Example 1:
# 
# 
# Input: words = ["i","love","leetcode","i","love","coding"], k = 2
# Output: ["i","love"]
# Explanation: "i" and "love" are the two most frequent words.
# Note that "i" comes before "love" due to a lower alphabetical order.
# 
# 
# Example 2:
# 
# 
# Input: words =
# ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4
# Output: ["the","is","sunny","day"]
# Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
# with the number of occurrence being 4, 3, 2 and 1 respectively.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 500
# 1 <= words[i].length <= 10
# words[i] consists of lowercase English letters.
# k is in the range [1, The number of unique words[i]]
# 
# 
# 
# Follow-up: Could you solve it in O(n log(k)) time and O(n) extra space?
# 
#

# @lc code=start
class Word:
    def __init__(self, word, time):
        self.word = word
        self.time = time
    
    def __lt__(self, o):
        if self.time != o.time: return self.time < o.time
        return self.word > o.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        cnt = Counter(words)
        heap = []
        for w in cnt:
            word = Word(w, cnt[w])
            if len(heap) < k:
                heap.append(word)
                if len(heap) == k:
                    heapify(heap)
            else:
                if word > heap[0]:
                    heapreplace(heap, word)
        heap.sort(reverse=True)
        return [x.word for x in heap]
# @lc code=end

