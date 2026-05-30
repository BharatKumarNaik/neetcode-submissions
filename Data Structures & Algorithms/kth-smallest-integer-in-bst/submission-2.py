# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # inorder traversal without dfs
        stack=[]
        arb=root
        while stack or arb:
            while arb:
                stack.append(arb)
                arb=arb.left
            arb=stack.pop()
            k-=1
            if k==0:
                return arb.val
            arb=arb.right

            
            