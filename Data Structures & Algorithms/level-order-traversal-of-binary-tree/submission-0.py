# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level={}
        lcount=0
        def dfs(root,lcount):
            nonlocal level
            if root==None:
                return
            if lcount not in level:
                level[lcount]=[]
            level[lcount].append(root.val)
            dfs(root.left,lcount+1)
            dfs(root.right,lcount+1)
        dfs(root,0)
        return list(level.values())