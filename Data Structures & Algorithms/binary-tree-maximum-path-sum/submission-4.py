# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # if a node is getting -ve value from it's child just ignore that child
        # and start a new life/path with other child.
        # every node must compute sum and store the max sum in the result
        # ignore the child if it comes back with -ve sum.
        # try to send only the positive child/grandchild value to ancestors.
        self.res = root.val
        def dfs(root):
            if root==None:
                return 0
            
            cur = root.val
            left = dfs(root.left)
            right = dfs(root.right)
            arb_total=cur
            if left>0:
                arb_total+=left
            if right>0:
                arb_total+=right
            self.res=max(self.res,arb_total)

            # It should be in a path structure so we must select either left or right
            # for previous node, as a path cannot be brached.
            # but for current node, path can move from left,root,right,
            # still there is no branch, hence in above conditions we are computing max with both left and right
            returnTotal=cur
            if left>0 and left>right:
                returnTotal+=left
            elif right>0 and right>=left:
                # make sure to include = sign as well
                returnTotal+=right
            return returnTotal
        dfs(root)
        return self.res
        