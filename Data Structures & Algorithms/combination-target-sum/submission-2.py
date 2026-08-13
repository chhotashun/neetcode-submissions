class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, total, curr):
            if total == target:
                res.append(curr.copy())
                return 
            if i >= len(nums) or total > target:
                return 
            curr.append(nums[i])
            total = total + nums[i]
            dfs(i, total, curr)
            total = total - nums[i]
            curr.pop()
            dfs(i + 1, total, curr)
            return res
        return dfs(0, 0, [])