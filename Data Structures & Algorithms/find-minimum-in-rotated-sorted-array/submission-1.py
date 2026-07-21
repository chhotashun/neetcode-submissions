class Solution:
    def findMin(self, nums: List[int]) -> int:
        # easy brute force code for fun
        res = nums[0]
        for i in nums:
            if i < res:
                res = i
        return res