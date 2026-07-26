# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # BFS on each tree together to check if it's matching or not
        q1 = deque([p])
        q2 = deque([q])
        while q1 and q2:
            for i in range(len(q1)):
                node1 = q1.popleft()
                node2 = q2.popleft()
                if node1 or node2:
                    if node1 and node2:
                        if node1.val != node2.val:
                            return False
                        q1.append(node1.left)
                        q2.append(node2.left)
                        q1.append(node1.right)
                        q2.append(node2.right)
                    else:
                        return False
        print(q1,q2)
        if len(q1)+len(q2)==0:
            return True
        return False