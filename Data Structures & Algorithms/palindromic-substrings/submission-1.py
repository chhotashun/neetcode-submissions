class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0 
        
        for i in range(len(s)):
            # odd length
            left, right = i, i
            while (left >= 0 and right < len(s)):
                if (s[left] == s[right]):
                    count += 1
                else:
                    break 
                left -= 1
                right += 1
            # even length substring 
            l, r = i, i + 1
            while (l >= 0 and r < len(s)):
                if (s[l] == s[r]):
                    count += 1
                else:
                    break
                l -= 1
                r += 1
        return count
