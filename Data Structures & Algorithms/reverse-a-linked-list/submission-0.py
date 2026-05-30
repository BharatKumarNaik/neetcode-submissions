# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur=head
        if cur==None:
            return cur
        prev=None
        while cur.next!=None:
            temp=cur.next
            cur.next=prev
            prev=cur
            cur=temp
            # print(temp.val,prev.val)
        cur.next=prev
        return cur
        