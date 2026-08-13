class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        def dfs(i):
            if i >= len(nums):
                res.append(subset.copy())
                #print(res)
                return 
            subset.append(nums[i])
            #print(subset)
            dfs(i + 1)
            subset.pop()
            dfs(i + 1)
            return res
        return dfs(0)