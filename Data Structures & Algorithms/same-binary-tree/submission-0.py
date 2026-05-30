# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        result=True
        def bmatch(r1,r2):
            nonlocal result
            if r1==None and r2==None:
                return
            if r1==None or r2==None:
                result=False
                return 
            if r1.val!=r2.val:
                result=False
                return 
            bmatch(r1.left,r2.left)
            bmatch(r1.right,r2.right)
        bmatch(p,q)
        return result