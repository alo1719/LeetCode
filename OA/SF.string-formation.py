import collections
from typing import List


def numWays(self, words: List[str], target: str) -> int:
    m, n = len(target), len(words[0])
    wordChars = []
    for j in range(n):
        wordChars.append(collections.Counter(word[j] for word in words))

    prev = [1] * (n + 1)
    for i in range(m - 1, -1, -1):
        cur = [0] * (n + 1)
        for j in range(n - 1, -1, -1):
            cur[j] = wordChars[j][target[i]] * prev[j + 1] + cur[j + 1]
        prev = cur

    return cur[0] % (10 ** 9 + 7)