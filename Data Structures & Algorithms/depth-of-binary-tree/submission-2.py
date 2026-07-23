# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        res = 0
        def dfs(root, count, result = 0):
            nonlocal res
            if not root:
                return 
            count += 1
            dfs(root.left, count)
            dfs(root.right, count)
            res = max(res, count)
            return result
        dfs(root, 0)
        return res