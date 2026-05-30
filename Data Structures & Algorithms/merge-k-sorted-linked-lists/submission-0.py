# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from functools import reduce
class Solution:
    def mergeTwo(self,l1,l2):
        cur1=l1
        cur2=l2
        res=ListNode()
        r_head=res
        while cur1!=None and cur2!=None:
            if cur1.val<cur2.val:
                temp=ListNode(cur1.val)
                cur1=cur1.next
            else:
                temp=ListNode(cur2.val)
                cur2=cur2.next
            res.next=temp
            res=res.next
        while cur1!=None:
            temp=ListNode(cur1.val)
            res.next=temp
            res=res.next
            cur1=cur1.next
        while cur2!=None:
            temp=ListNode(cur2.val)
            res.next=temp
            res=res.next
            cur2=cur2.next
        return r_head.next
            
            
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # insertion sort
        if len(lists)==0:
            return 
        temp=reduce(lambda x,y: self.mergeTwo(x,y),lists)
        return temp