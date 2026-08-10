class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # approach is to make stones a max heap
        stones = [-s for s in stones]
        heapq.heapify(stones)
        while(len(stones)) > 1:
            first = heapq.heappop(stones) # x
            second = heapq.heappop(stones) # y
            print("x < y: ", first, second)
            if first < second: # if x < y
                heapq.heappush(stones, first - second)
        stones.append(0)
        return abs(stones[0])