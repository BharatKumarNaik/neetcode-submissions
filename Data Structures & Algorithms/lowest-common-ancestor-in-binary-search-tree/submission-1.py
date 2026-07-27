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
        global parents
        parents = []
        pp = []
        qp = []
        def getParents(root,node):
            global parents
            if root==None:
                return False
            if root.val==node.val:
                parents.append(root)
                return True
            lfound=getParents(root.left,node)
            rfound=getParents(root.right,node)
            found = lfound or rfound
            if found:
                parents.append(root)
            return found
        getParents(root,p)
        pp=parents.copy()
        parents=[]
        getParents(root,q)
        qp=parents
        if len(pp)<len(qp):
            qp = set([x.val for x in qp])
            for i in pp:
                if i.val in qp:
                    return i
        else:
            pp = set([x.val for x in pp])
            for i in qp:
                if i.val in pp:
                    return i
