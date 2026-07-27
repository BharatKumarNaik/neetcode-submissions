# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # Brute Force: works even when it's not BST
        # get all the parent node of p including itself
        # get all the parent node of q including itself
        # iterate through each items of the list, wherever we find the first common parent is the least common parent.
        # O(n) + O(n) + O(min(pp_n,qp_n))
        
        # Optimal: Since it's a Binary Search Tree
        # if max value between p and q is in left side of root, max value arrives first in root.left
        # if min value between p and q is in right side of root, min value arrives first in root.right
        # O(h)
        if not root or not p or not q:
            return None
        
        if (max(p.val, q.val) < root.val):
            # max value come first
            return self.lowestCommonAncestor(root.left, p, q)
        elif (min(p.val, q.val) > root.val):
            # min value come first in right side of the node
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root