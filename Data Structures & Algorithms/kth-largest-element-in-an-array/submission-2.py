class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # optimise to what
        # o(nlogk) time and o(k) space
        # using min heap makes sense 
        # use min heap to sort the array
        # return kth largest 
        heapq.heapify(nums)
        #print(nums)
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]