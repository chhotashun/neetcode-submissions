class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # i am the biggest idiot should've used set non repeating 
        hashset = set()
        left, window_len = 0, 0
        for right in range(len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left += 1
            hashset.add(s[right])
            tmp_len = (right - left) + 1
            window_len = max(tmp_len, window_len)
        return window_len