# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # time and space complexity- o(n)
        if not root: 
            return []
        res = []
        queue = deque([root])
        print("how was while queue run: ", queue)
        while queue:
            tmp_list = []
            length = len(queue)
            for i in range(len(queue)):
                node = queue.popleft()
                tmp_list.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(tmp_list)
        return res