# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        #     1
        #   2    3
        # 5  6  7  8
        # preorder: root,left,right
        # inorder: left,root,right
        # root=preorder.popleft()
        # find root in inorder
        # all element left to root index in inorder are left right side are right
        if not preorder or not inorder:
            return None
        root = TreeNode(preorder[0])
        rootInorderIndex = inorder.index(preorder[0]) # Expensive
        root.left = self.buildTree(preorder[1:rootInorderIndex+1],inorder[:rootInorderIndex])
        root.right = self.buildTree(preorder[rootInorderIndex+1:],inorder[rootInorderIndex+1:])
        return root