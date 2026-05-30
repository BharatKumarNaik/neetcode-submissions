# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def bmatch(r1,r2,result=True):
            if r1==None and r2==None:
                return result
            if r1==None or r2==None:
                result=False
                return result
            if r1.val!=r2.val:
                result=False
                return result
            result=bmatch(r1.left,r2.left,result) and bmatch(r1.right,r2.right,result)
            return result
        def find_subroot(r1,r2,result=False):
            if r1==None or r2==None:
                return result
            if r1.val==r2.val:
                result=bmatch(r1,r2)
            return result or find_subroot(r1.left,r2,result) or find_subroot(r1.right,r2,result)
        return find_subroot(root,subRoot)

                