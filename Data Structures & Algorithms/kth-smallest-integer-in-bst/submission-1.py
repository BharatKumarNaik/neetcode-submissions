# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arb_k=1
        k_flag=0
        result=root.val
        # inorder traversal 
        def preorder(root):
            nonlocal arb_k,k_flag,result
            if root==None:
                k_flag=1
                return

            preorder(root.left)
            # print(root.val)
            if arb_k==k:
                result=root.val
            if k_flag==1:
                arb_k+=1
            preorder(root.right)
            return
        preorder(root)
        return result

            
            