# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self,):
        self.res=0
    def rec(self,root):
        if root==None:
            return 0
        
        l=self.rec(root.left)
        r=self.rec(root.right)
        arb_res = max(l,r)
        self.res = max(self.res,l+r)
        return arb_res+1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.rec(root)
        return self.res