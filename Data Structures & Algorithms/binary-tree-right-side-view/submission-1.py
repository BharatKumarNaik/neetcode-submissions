# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # BFS with each levels last node val
        queue=[]
        result=[]
        queue.append(root)
        while queue:
            n=len(queue)
            level=[]
            for i in range(n):
                first=queue.pop(0)
                if first:
                    level.append(first.val)
                    queue.append(first.left)
                    queue.append(first.right)
            if level:
                result.append(level[-1])
        return result