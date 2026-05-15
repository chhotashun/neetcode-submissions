class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hashset solution 
        if (len(s) == 0):
            return 0
        count = 1
        max_count = 1
        left = 0
        right = 1
        hashset = set()
        hashset.add(s[left])
        while (right < len(s)):
            if (s[right] in hashset):
                left += 1
                right = left
                hashset.clear()
                max_count = 0
            max_count += 1
            if (max_count > count):
                count = max_count 
            hashset.add(s[right])
            right += 1
        return count
        