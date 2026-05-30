# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        result=[]
        def dfs(root):
            nonlocal result
            if root==None:
                result.append('None')
                return
            result.append(str(root.val))
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return ','.join(result)
            
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        values=data.split(',')
        i=0
        def dfs():
            nonlocal i
            if values[i]=='None':
                i+=1
                return None
            base=TreeNode(int(values[i]))
            i+=1
            base.left=dfs()
            base.right=dfs()
            return base
        return dfs()
    


