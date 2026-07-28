# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # Iterative DFS
        # inorder traversal
        global arr
        arr=[]
        def DFS(root):
            if not root:
                return 

            DFS(root.left)
            global arr
            arr.append(root.val)
            DFS(root.right)
        DFS(root)
        # print(arr)
        return arr[k-1]
        