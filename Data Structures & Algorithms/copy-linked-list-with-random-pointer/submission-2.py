"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashMap = {None:None} # Base: for None address None is the copy version

        cur = head
        while cur:
            cpy = Node(cur.val)
            hashMap[cur] = cpy
            cur=cur.next
        
        cur=head
        while cur:
            cpy = hashMap[cur]
            cpy.next = hashMap[cur.next]
            cpy.random = hashMap[cur.random]
            cur = cur.next
        
        return hashMap[head]