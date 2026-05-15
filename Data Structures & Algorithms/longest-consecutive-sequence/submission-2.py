class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashmap = {}
        res = 0
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        for i in nums:
            count = 1
            if ((i - 1) in hashmap):
                continue 
            while ((i + 1) in hashmap):
                print("i is : ", i)
                count += 1
                i += 1
            res = max(count, res)
            print("result is: ", res)
        return res