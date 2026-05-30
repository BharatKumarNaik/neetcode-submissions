# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # brute force 
        # find the len of the linked list
        # pop out the len-n th node
        length=0
        cur=head
        while cur!=None:
            length+=1
            cur=cur.next
        arb=0
        cur=head
        prev=None
        print(length-n)
        while arb!=length-n:
            prev=cur
            cur=cur.next
            arb+=1
        temp=cur.next
        if prev==None and length<=1:
            return None
        elif prev==None and length>1:
            head=head.next
            return head
        prev.next=temp
        return head
        