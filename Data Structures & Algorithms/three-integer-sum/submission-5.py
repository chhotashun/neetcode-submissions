class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            if (left > len(nums) - 1):
                break
            if (i > 0 and nums[i] == nums[i - 1]):
                continue
            while (left < right):
                sum = nums[i] + nums[left] + nums[right]
                if (nums[left] == nums[left + 1]):
                    left += 1
                if (nums[right] == nums[right - 1]):
                    right -= 1
                if (sum < 0):
                    left += 1
                    sum = nums[i] + nums[left] + nums[right]
                elif (sum > 0):
                    right -= 1
                    sum = nums[i] + nums[left] + nums[right]
                else:
                    result.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        return result