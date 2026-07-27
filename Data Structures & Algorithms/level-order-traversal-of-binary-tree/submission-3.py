# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # BFS
        q = deque([(0,root)])
        res = {}
        while q:
            level,node = q.popleft()
            if not node:
                continue
            q.append((level+1,node.left))
            q.append((level+1,node.right))
            if level not in res:
                res[level]=[]
            res[level].append(node.val)
        return list(res.values())
