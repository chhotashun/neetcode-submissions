class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hashmap = {}
        left, window_len, freq = 0, 0, 0
        for right in range(len(s)):
            hashmap[s[right]] = hashmap.get(s[right], 0) + 1
            freq = max(freq, hashmap[s[right]])
            while ((right - left) + 1- freq) > k:
                hashmap[s[left]] -= 1
                left += 1
            window_len = max(right - left + 1, window_len)
        return window_len 