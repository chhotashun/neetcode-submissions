class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == val:
                nums.pop(i)
                i = i - 1
                n = n - 1
            i += 1
        return len(nums)