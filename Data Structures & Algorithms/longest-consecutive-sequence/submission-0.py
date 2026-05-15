class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set()
        for i in nums:
            hashset.add(i)
        longest = 0
        for x in nums:
            max = 0
            if (x - 1 in nums):
                continue 
            while (x in hashset):
                max += 1
                if (max > longest):
                    longest = max
                x += 1
        return longest