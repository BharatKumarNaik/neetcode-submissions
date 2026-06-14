# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        arb = head
        if not arb:
            return None
        prev = None
        while arb.next:
            temp = arb.next
            arb.next = prev
            prev = arb
            arb = temp
        arb.next = prev
        return arb
