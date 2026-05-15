# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        q1 = deque([(root, float("-inf"), float("inf"))])
        while (q1):
            node, left, right = q1.popleft()
            if not (left < node.val < right):
                return False
            if (node.left):
                q1.append((node.left, left, node.val))
            if (node.right):
                q1.append((node.right, node.val, right))
        return True