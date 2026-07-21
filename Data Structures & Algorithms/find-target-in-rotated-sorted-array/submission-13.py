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
            if nums[mid] >= nums[left]:
                if nums[left] <= target <= nums[mid]:
                        right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] <= target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return -1