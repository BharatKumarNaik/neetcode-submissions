# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Iterative DFS:
        # DFS to get the hight of each side of the node
        # Iterative cuz, the moment we find out that there is bigger hight gap then 1
        # between left and right sub-tree I can return as Flase.
        if root==None:
            return True
            
        stack = [root]
        mp={None:(0,0)}
        while stack:
            node=stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                left_l,left_r = mp[node.left]
                right_l,right_r = mp[node.right]
                left_height = max(left_l,left_r)+1
                right_height = max(right_l,right_r)+1
                if abs(left_height-right_height)>1:
                    return False
                mp[node]=(left_height,right_height)
        return True
                