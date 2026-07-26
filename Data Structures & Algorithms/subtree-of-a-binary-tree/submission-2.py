# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution: 
    def isMatch(self,root1,root2):
        # root2 must be considered as base root
        # as root1 may contain extra nodes compared to root2
        q1=deque([root1])
        q2=deque([root2])
        while q2:
            node1=q1.popleft()
            node2=q2.popleft()
            if node1 or node2:
                if node1 and node2:
                    if node1.val==node2.val:
                        q1.append(node1.left)
                        q2.append(node2.left)
                        q1.append(node1.right)
                        q2.append(node2.right)
                    else:
                        return False
                else:
                    return False
        if len(q2)==0:
            return True
        return False


    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Iterative DFS to find the matching node val
        # Once match found send it to isMatch function, which uses BFS to find the similarity
        stack = [root]
        mp={None} #just a set to keep track of traversed node
        while stack:
            node = stack[-1]
            if node.left and node.left not in mp:
                stack.append(node.left)
            elif node.right and node.right not in mp:
                stack.append(node.right)
            else:
                node = stack.pop()
                mp.add(node)
                if node.val==subRoot.val:
                    status = self.isMatch(node,subRoot)
                    if status:
                        return status
        return False
