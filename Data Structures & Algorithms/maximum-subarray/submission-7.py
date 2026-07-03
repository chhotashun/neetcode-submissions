class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        tmp = 0
        for i in nums:
            if tmp < 0:
                tmp = 0
            tmp += i
            res = max(res, tmp)
        return res