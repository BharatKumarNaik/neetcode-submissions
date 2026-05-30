# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Optimal
        left,right=head,head
        while n>0:
            right=right.next
            n-=1
        prev=None
        while right:
            prev=left
            left=left.next
            right=right.next
        if prev==None:
            head=head.next
        else:
            prev.next=left.next
        return head
        