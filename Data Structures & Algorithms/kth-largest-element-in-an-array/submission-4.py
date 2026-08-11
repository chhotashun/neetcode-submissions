class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # optimise to what
        # o(nlogk) time and o(k) space
        # using min heap makes sense 
        # use min heap to sort the array
        # return kth largest 
        # this is o(nlgn) code and o(1) space similar to sorting not optimal 
        # to make it optimal we need to keep heap of size k while processing nodes from nums that gives it o(nlgk)
        heap = []
        for item in nums:
            heapq.heappush(heap, item)
            if len(heap) > k:
                heapq.heappop(heap)
        #print(heap)
        return heap[0]