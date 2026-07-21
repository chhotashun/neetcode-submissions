class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] == target:
            return 0
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            print("mid value: ", mid)
            if target == nums[mid]:
                return mid 
            print("Condition 1: ", target >= nums[left] and target <= nums[mid])
            if target >= nums[left] and target <= nums[mid]:
                right -= 1
            else:
                left += 1
        return -1