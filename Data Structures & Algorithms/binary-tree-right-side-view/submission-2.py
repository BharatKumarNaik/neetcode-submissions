# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # DFS but parsing right node first, 
        # and we need keep track of the level.
        # since we are parsing right node first, it will ensure we see right side first.
        # if not there then move to left node, and if the left node's level is less then max reached level just move forward.
        # else store that and increment the level
        global level
        level = 0
        global res
        res = []
        def rightFirstDFS(root,l):
            if root==None:
                return None
            global level
            global res
            if l>level:
                res.append(root.val)
                level=l
            rightFirstDFS(root.right,l+1)
            rightFirstDFS(root.left,l+1)
        rightFirstDFS(root,level+1)
        return res

