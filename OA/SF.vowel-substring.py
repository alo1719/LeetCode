class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        ans, last_consonant = 0, -1
        last_seen_vowels = {v: -1 for v in "aeiou"}
        for i, x in enumerate(word):
            if x in last_seen_vowels:
                last_seen_vowels[x] = i
                ans += max(min(last_seen_vowels.values()) - last_consonant, 0)
            else:
                last_consonant = i
        return ans
