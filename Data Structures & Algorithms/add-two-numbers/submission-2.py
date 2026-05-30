# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        cur1=l1
        cur2=l2
        result=ListNode()
        cur=result
        carry=0
        while cur1!=None and cur2!=None:
            temp=cur1.val+cur2.val+carry
            if temp>=10:
                carry=temp//10
            else:
                carry=0
            val=ListNode(temp%10)
            cur.next=val
            cur=cur.next
            cur1=cur1.next
            cur2=cur2.next
        while cur1!=None:
            temp=cur1.val+carry
            if temp>=10:
                carry=temp//10
            else:
                carry=0
            val=ListNode(temp%10)
            cur.next=val
            cur=cur.next
            cur1=cur1.next
        while cur2!=None:
            temp=cur2.val+carry
            if temp>=10:
                carry=temp//10
            else:
                carry=0
            val=ListNode(temp%10)
            cur.next=val
            cur=cur.next
            cur2=cur2.next
        if carry!=0:
            val=ListNode(carry)
            cur.next=val
        result=result.next
        return result
            