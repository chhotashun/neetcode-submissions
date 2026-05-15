class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        area = 0
        while (left < right):
            width = right - left 
            length = min(heights[left], heights[right])
            max1 = length * width
            if (max1 > area):
                area = max1
            if (heights[left] < heights[right]):
                left += 1
            else:
                right -= 1
        return area