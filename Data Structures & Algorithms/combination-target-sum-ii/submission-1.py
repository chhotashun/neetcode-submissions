class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()
        def dfs(i, total, curr):
            if total == target:
                res.append(curr.copy())
                #print(res)
                return 
            if i >= len(candidates) or total > target:
                return 
            curr.append(candidates[i])
            #print(curr)
            dfs(i + 1, total + candidates[i], curr)
            #print("i here: ", i)
            curr.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            #print(curr)
            dfs(i + 1, total, curr)
        dfs(0, 0, [])
        return res