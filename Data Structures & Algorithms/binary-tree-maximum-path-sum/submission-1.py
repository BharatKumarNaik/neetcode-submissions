# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root!=None:
            result=root.val
        else:
            return
        def dfs(root):
            if root==None:
                return 0
            # base path
            base=root.val
            left=dfs(root.left)
            right=dfs(root.right)
            if left<0:
                left=0
            if right<0:
                right=0

            LR=base+left+right
            
            # max path
            m_path=base+max(left,right)
            nonlocal result
            result=max([result,m_path,LR])
            # print(m_path,LR)
            return m_path
        dfs(root)
        return result
