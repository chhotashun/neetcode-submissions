class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # dp top down similar to house robber 
        # first lets do brute focr 
        # approach- for each value calculate the sum in inner loop 
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            res = max(nums[0], nums[1])
            return res 
        res = nums[0]
        for i in range(len(nums)):
            j = i + 1
            tmp = nums[i]
            #print("our j value is: ", j)
            while (j < len(nums)):
                #print("index i: ", nums[i], "index j ", nums[j])
                tmp = tmp + nums[j]
                #print("the sum calculated is: \n", tmp)
                if (tmp > res):
                    res = tmp
                j += 1
            if (tmp > res):
                res = tmp
        #print("our result at end: ", res)
        return res

        