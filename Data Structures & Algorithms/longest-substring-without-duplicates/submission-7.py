class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Hashset solution 
        hashset = set()
        left = 0
        count = 0
        max_count = 0
        for right in range(len(s)):
            while (s[right] in hashset):
                hashset.remove(s[left])
                left += 1
                max_count -= 1
            hashset.add(s[right])
            max_count += 1
            if (max_count > count):
                count = max_count 
        return count 