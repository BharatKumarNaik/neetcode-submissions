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
        # optimal approach
        # using hashmap
        cur=head
        repo={}
        # store independent nodes in a hashmap
        while cur!=None:
            repo[cur]=Node(cur.val)
            cur=cur.next
        
        copy=Node(0)
        c_head=copy
        cur=head
        # copy=hasmap[cur_node]
        # copy.random=hasmap[cur_node.random]
        while cur!=None:
            copy.next=repo[cur]
            if cur.random==None:
                copy.next.random=None
            else:
                copy.next.random=repo[cur.random]
            copy=copy.next
            cur=cur.next
        return c_head.next
