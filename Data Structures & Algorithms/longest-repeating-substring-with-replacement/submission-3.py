class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        window_len = 0
        left = 0
        freq = 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            freq = max(freq, hashmap[s[right]])
            while (right - left + 1) - freq > k:
                hashmap[s[left]] -= 1
                left += 1
            window_len = max(window_len, right - left + 1)
        return window_len