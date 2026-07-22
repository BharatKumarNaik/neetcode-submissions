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
        # A->A'->B->B'->C->C'
        cur = head
        while cur:
            cpy_node = Node(cur.val)
            cpy_node.next = cur.next
            cur.next = cpy_node
            cur = cur.next.next
        
        # now we have copied the cpy_node's values
        # for connecting random address/node
        cur = head
        while cur:
            # cur.next is A' and it's random should be A's random's next node, which is again a copied node
            if cur.random:
                cur.next.random = cur.random.next
            else:
                cur.next.random = None
            cur = cur.next.next
        
        # Now we just need to disconnect the A and A' part
        cur = head
        cpy = Node(0) #Dummy head
        cpy_head = cpy
        while cur:
            temp=cur.next # A'
            cur.next = cur.next.next # A-> A'-> B ==> A->B
            cpy.next = temp # 0->A' 
            cpy = cpy.next  # 0->A' (cpy pointed to A')
            cur = cur.next # cur poimted to B
        
        return cpy_head.next

        