# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validity(left,root,right):
            if root==None:
                return True
            if not(left<root.val<right):
                return False
            
            return validity(left,root.left,root.val) and validity(root.val,root.right,right)
        return validity(-1001,root,1001)
        