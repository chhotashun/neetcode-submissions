# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q1 = deque([root])
        result = []
        while (q1):
            length = len(q1)
            level = []
            for i in range(length):
                node = q1.popleft()
                if node:
                    level.append(node.val)
                    q1.append(node.left)
                    q1.append(node.right)
            if level:
                result.append(level)
        return result
