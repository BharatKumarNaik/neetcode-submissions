# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        def rec(arb):
            if not arb: #if None
                return 1,0
            k,brk = rec(arb.next)
            if brk==0:
                if k>n:
                    # reached the one node before the deletion node
                    arb.next=arb.next.next
                    return 1,1
                else:
                    return k+1,0 
            return 1,1
        k,brk=rec(head)
        if brk==0:
            # single element linked list
            head = head.next
        return head
