# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    #DFS Solution
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if (not p and not q):
            return True
        if (not p or not q):
            return False
        if (p.val != q.val):
            return False 
        tmp1 = self.isSameTree(p.left, q.left)
        tmp2 = self.isSameTree(p.right, q.right)
        return tmp1 and tmp2