class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap1 = {}
        for item in nums:
            hashmap1[item] = hashmap1.get(item, 0) + 1
        bucket = [[] for i in range(len(nums) + 1)]
        for key, value in hashmap1.items():
            bucket[value].append(key)
        result = []
        counter = len(bucket) - 1
        for i in range(len(bucket) - 1, -1, -1):
            for num in bucket[i]:
                result.append(num)
                if (len(result) == k):
                    return result
        return result