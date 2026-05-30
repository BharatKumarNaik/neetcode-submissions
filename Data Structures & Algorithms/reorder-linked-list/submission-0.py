# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # find mid pointer
        # since all the reverse traversal vals come after mid pointer
        slow=head
        fast=head
        while fast.next != None and fast.next.next !=None:
            slow=slow.next
            fast=fast.next.next
        mid=slow
        
        front=head
        while front.next !=None and front.next.next!=None:
            temp=front.next
            arb=mid
            while arb.next.next!=None:
                arb=arb.next
            # at the end arb will have last but one element
            front.next=arb.next
            arb.next.next=temp
            arb.next=None
            front=front.next.next
            
            
            
