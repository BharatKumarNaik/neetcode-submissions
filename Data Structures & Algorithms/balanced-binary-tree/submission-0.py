# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # differ in height no more than 1
        result=True
        def dfs(root):
            if root==None:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)
            if left-right>1 or right-left>1:
                nonlocal result
                result=False
            return 1+max(left,right)
        dfs(root)
        return result
