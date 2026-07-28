# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        # while doing DFS send max of all the node values till that point.
        # when new new node is detected check if that new node's value is greater then the max val.
        # if so increment the count by one and move ahead.
        global count
        count = 1
        def DFS(root,rcnMax):
            if root==None:
                return None
            # print(root.val,rcnMax)
            global count
            if root.val>=rcnMax:
                count+=1
                rcnMax = root.val
            # print(count)
            DFS(root.left,rcnMax)
            DFS(root.right,rcnMax)
        DFS(root.left,root.val)
        DFS(root.right,root.val)
        return count