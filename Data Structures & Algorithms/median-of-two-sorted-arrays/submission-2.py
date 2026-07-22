class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # brute force- combine into one array and sort 
        nums = sorted(nums1 + nums2)
        print(nums)
        n = len(nums)
        # odd case
        if n % 2 != 0:
            median = (n + 1) // 2
            return nums[median - 1]
        else:
            # for even numbers 
            median = (n // 2) 
            median1 = (n // 2) + 1
            return (nums[median - 1] + nums[median1 - 1]) / 2