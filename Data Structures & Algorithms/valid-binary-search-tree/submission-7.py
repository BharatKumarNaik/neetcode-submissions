# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def DFS(root,l,r):
            if not root:
                return True
            if not(l<root.val<r):
                return False
            # lowerbound, upperbound
            # left nodes must not be greater then root.val
            lstatus=DFS(root.left,l,root.val)
            # right nodes must not be lesser then root.val
            rstatus=DFS(root.right,root.val,r)
            return lstatus and rstatus
        return DFS(root,float("-inf"),float("inf"))