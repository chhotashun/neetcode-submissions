class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []
        def dfs(curr, used):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return
            for j in range(len(nums)):
                if used[j]:
                    continue 
                curr.append(nums[j])
                used[j] = True
                dfs(curr, used)
                curr.pop()
                used[j] = False
            return res
        dfs([], [False for i in range(len(nums))])
        return res
            