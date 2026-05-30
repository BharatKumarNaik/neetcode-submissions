# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(root,left,right):
            if root==None:
                return True
            if not (left<root.val<right):
                return False
            return validity(root.left,left,root.val) and validity(root.right,root.val,right)
        return validity(root,float('-inf'),float('inf'))
        