# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        #DFS In order
        res = []

        def dfs(root):
            if (root is None):
                return 
            dfs(root.left)
            res.append(root.val)
            print(res)
            dfs(root.right)
            print(res)
            return res
        dfs(root)
        return res[k - 1]
