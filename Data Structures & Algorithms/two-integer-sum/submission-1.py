class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for index, value in enumerate(nums):
            found = target - value
            if found in hashmap:
                return [hashmap[found], index]
            hashmap[value] = index 
        return