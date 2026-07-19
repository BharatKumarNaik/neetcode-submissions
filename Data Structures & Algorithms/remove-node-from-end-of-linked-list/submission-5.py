# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Two pointer solution
        dummy = ListNode(0,head)
        follower = dummy
        first = head
        while n>0:
            n-=1
            first = first.next
        
        # here follower will always stay n+1 distance away from first pointer
        # cuz only first pointer started above
        # and follower started from behind the head
        while first:
            first=first.next
            follower=follower.next
        
        follower.next = follower.next.next
        return dummy.next