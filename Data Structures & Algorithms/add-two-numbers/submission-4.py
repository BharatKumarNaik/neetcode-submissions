# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res_head = ListNode(val=0)
        res = res_head
        reminder = 0
        while l1 and l2:
            temp = l1.val + l2.val + reminder
            if temp>9:
                reminder = temp//10
                temp = temp%10
            else:
                reminder = 0
            res.next = ListNode(val=temp)
            l1 = l1.next
            l2 = l2.next
            res = res.next

        if l1:
            bigger_list = l1
        else:
            bigger_list = l2
        
        while bigger_list:
            temp = bigger_list.val + reminder
            if temp>9:
                reminder = temp//10
                temp = temp%10
            else:
                reminder = 0
            res.next = ListNode(val=temp)
            bigger_list = bigger_list.next
            res = res.next

        while reminder>0:
            temp=reminder%10
            res.next = ListNode(temp)
            res = res.next
            reminder = reminder//10

        res_head=res_head.next
        return res_head

