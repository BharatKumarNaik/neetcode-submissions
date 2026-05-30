# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # [x,2,3,4]
        # [2,x,3,4]
        if not preorder or not inorder:
            return None
        
        root=TreeNode(preorder.pop(0))
        i_mid=inorder.index(root.val)

        root.left=self.buildTree(preorder[:i_mid],inorder[:i_mid])
        root.right=self.buildTree(preorder[i_mid:],inorder[i_mid+1:])
        return root