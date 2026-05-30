"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        datastore={}
        def dfs(arb):
            if arb is None:
                return None
            if arb in datastore:
                return datastore[arb]
            temp=Node(arb.val)
            datastore[arb]=temp
            for n in arb.neighbors:
                temp.neighbors.append(dfs(n))
            return temp
        return dfs(node)