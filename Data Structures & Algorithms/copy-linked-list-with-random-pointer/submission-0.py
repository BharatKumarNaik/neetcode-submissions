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
        # Brute force
        # perform copy operation for normal linked list
        # keep all the random value as null
        # next iterate through every element of both linked list
        # if main LL random node is connected to another node 
        # navigate to that node and search in both direction (left and right)
        # to find how far does that node is located
        # perform the same in the copied LL as well to achieve the result
        c_head=Node(0)
        c_cur=c_head
        cur=head
        while cur!=None:
            arb_c=Node(cur.val)
            c_cur.next=arb_c
            c_cur=c_cur.next
            cur=cur.next
        c_head=c_head.next
        c_cur=c_head
        cur=head
        while cur!=None or c_cur!=None:
            rand=cur.random
            # move left or right untill we get the mapping node
            if rand==None:
                c_cur.random=None
            temp=head
            distance=0
            while temp!=None:
                if temp==rand:
                    break
                distance+=1
                temp=temp.next
            temp=c_head
            c_distance=0
            while temp!=None:
                if c_distance==distance:
                    c_cur.random=temp
                    break
                c_distance+=1
                temp=temp.next
            cur=cur.next
            c_cur=c_cur.next
        return c_head
