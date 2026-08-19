class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # subset question
        # two pointer as well left and right 
        res = []
        substring = []
        def dfs(i):
            if i >= len(s):
                res.append(substring.copy())
                return
            for j in range(i, len(s)):
                if self.isPali(s,i,j):
                    substring.append(s[i:j+1])
                    dfs(j+1)
                    substring.pop()
        dfs(0)
        #print(res)
        return res
    def isPali(self, s, i, j):
        while (i < j):
            if s[i] != s[j]:
                return False
            i, j = i + 1, j - 1
        return True
