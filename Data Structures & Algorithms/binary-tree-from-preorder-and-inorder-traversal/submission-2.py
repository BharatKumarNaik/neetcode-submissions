# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # preorder: root, left, right
        # inorder: left, root, right
        # preorder = [1,2,3,4], inorder = [2,1,3,4]
        # root = preorder[0]
        # check inorder: all the values left to preorder[0] is left right to preorder[0] is right
        # inorder = [2,   1,  3,4]
        # and number of values between, 0 to root.val index in inorder can be used to seggregate preorder as well
        # so, preorder= [1,  2,   3,4]
        # exp of preorder: in inorder we have 1 value left to root.val
        # hence in preorder: 1 value from first node is considered as left. it can be n nodes
        # 2 vals from right side of root.val in inorder can be used to decide,
        # 2 values after 1 left value seperation in preorder are right values.
        enumerated_inorder = {x:i for i,x in enumerate(inorder)}
        self.preorder_arbIndex = 0
        def build(l,r):
            if l>r:
                return None
            root = TreeNode(preorder[self.preorder_arbIndex])
            self.preorder_arbIndex+=1
            root_inorder_index = enumerated_inorder[root.val]
            root.left = build(l,root_inorder_index-1)
            root.right = build(root_inorder_index+1, r)
            return root
        return build(0,len(inorder)-1)