class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # stupid n log n 
        # this is so fucking stupid have to remember bucket sort
        hashmap = {}
        for item in nums:
            hashmap[item] = hashmap.get(item, 0) + 1
        print(hashmap)
        res = []
        sorted_map = sorted(hashmap, key = hashmap.get, reverse = True)
        print(sorted_map)
        left = 0
        while k > 0:
            res.append(sorted_map[left])
            k -= 1
            left += 1
        return res


