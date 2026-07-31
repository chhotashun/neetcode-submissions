class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # easiest brute force is hashset
        hashset = set()
        for item in nums:
            if item in hashset:
                return item 
            hashset.add(item)