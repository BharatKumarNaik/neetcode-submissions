# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1==None:
            return list2
        elif list2==None:
            return list1
        cur1=list1
        cur2=list2
        res=ListNode()
        rhead=res
        while cur1!=None and cur2!=None:
            # print(cur1.val,cur2.val)
            if cur1.val<=cur2.val:
                res.next=cur1
                cur1=cur1.next
            else:
                res.next=cur2
                cur2=cur2.next
            # print(res.next.val)
            res=res.next
        while cur1!=None:
            res.next=cur1
            cur1=cur1.next
            res=res.next
        while cur2!=None:
            res.next=cur2
            cur2=cur2.next
            res=res.next
        return rhead.next
