class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # i cant come with these problems on my own 
        res = max(nums)
        curMax, curMin = 1,1 

        for i in nums:
            if i == 0:
                curMax, curMin = 1, 1
                continue 
            tmp = i * curMax
            curMax = max(curMax * i, curMin * i, i)
            curMin = min(tmp, curMin * i, i)
            res = max(curMax, res)
        return res