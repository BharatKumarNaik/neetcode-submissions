# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Using BFS
        res=[]
        queue=[]
        queue.append(root)
        while queue:
            n=len(queue)
            level=[]
            for i in range(n):
                first=queue.pop(0)
                if first!=None:
                    level.append(first.val)
                    queue.append(first.left)
                    queue.append(first.right)
            if level:
                res.append(level)
        return res