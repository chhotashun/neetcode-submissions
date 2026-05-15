class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # Python lists are fucking dynamic I forgot 
        i = 0 
        n = len(nums)
        while i < n:
            nums.append(nums[i])
            i += 1
            #print(nums)
        return nums