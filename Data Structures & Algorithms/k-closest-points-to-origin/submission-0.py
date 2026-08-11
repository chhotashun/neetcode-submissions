class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
      # closest point min or max heap
      # variation or extension of kth largest element 
      # use min heap to return kth closest points to the origin 
      minHeap = []
      for x,y in points:
        dist = (x**2) + (y**2)
        minHeap.append([dist,x,y])
      print(minHeap)
      heapq.heapify(minHeap)
      res = []
      while k > 0:
        dist, x, y = heapq.heappop(minHeap)
        res.append([x,y])
        k -= 1
        # just use a tuple (dist, x, y) and store in heap, heapify and pop
      return res 
