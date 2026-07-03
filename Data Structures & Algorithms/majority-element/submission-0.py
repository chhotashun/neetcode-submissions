class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        hashmap = {}
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        for i in hashmap:
            if hashmap[i] > (math.floor(len(nums) / 2)):
                return i
        