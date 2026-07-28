# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS
        # inorder traversal
        global arb,res
        arb=0
        def DFS(root):
            if not root:
                return 

            DFS(root.left)
            global arb,res
            arb+=1
            if arb==k:
                res= root.val
            DFS(root.right)
        DFS(root)
        # print(arr)
        return res
        