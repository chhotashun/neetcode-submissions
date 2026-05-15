class Solution:
    def rob(self, nums: List[int]) -> int:
        # first nad last houses are neighbour
        # so cannot rob first and last house now 
        # same logic one extra base case for len(arr) <= 3
        # run it twice 
        # first run with 2 
        # next with 6 
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        rob1, rob2 = 0, 0
        temp1, temp2 = 0, 0
        for n in range(0, len(nums) - 1):
            temp1 = max(nums[n] + rob1, rob2)
            rob1 = rob2 
            rob2 = temp1
        
        temp_rob1, temp_rob2 = 0, 0
        for n in range(1, len(nums)):
            temp2 = max(nums[n] + temp_rob1, temp_rob2)
            temp_rob1 = temp_rob2 
            temp_rob2 = temp2 
        if (temp1 > temp2):
            return temp1 
        return temp2 
