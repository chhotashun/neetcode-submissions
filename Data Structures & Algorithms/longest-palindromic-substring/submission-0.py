class Solution:
    def longestPalindrome(self, s: str) -> str: 
        # i am a bum 
        res = ""
        resLen = 0

        for i in range(len(s)):
            left, right = i, i 
            while left >= 0 and right < len(s) and s[left] == s[right]:
                if (right - left + 1) > resLen:
                    res = s[left:right+1]
                    resLen = right - left + 1
                left -= 1
                right += 1
            # even length 
            l, r = i, i + 1
            while l >= 0 and r < len(s) and s[r] == s[l]:
                if (r - l + 1) > resLen:
                    res = s[l:r+1]
                    resLen = r - l + 1
                l -= 1
                r += 1
        return res
