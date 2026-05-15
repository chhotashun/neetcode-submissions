class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        if len(nums) == 0:
            return []
        
        res_len = 2*len(nums)
        result = [0 for i in range(res_len)]
        #print(res_len, result)
        i, pointer = 0, 0
        while i < len(result):
            result[i] = nums[pointer]
            #print("updated list: ", result)
            i += 1
            pointer += 1
            if (pointer >= len(nums)):
                pointer = 0
            #print(i, pointer)
        return result