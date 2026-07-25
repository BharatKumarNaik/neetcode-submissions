# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseLL(self,head,tail):
        arb = head
        prev = None
        while arb!=None:
            temp = arb.next
            arb.next = prev
            prev = arb
            arb = temp
            # print(arb.val)
        return tail,head
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Two pointer method to get the k window
        # second pointer should traverse for k steps
        # then second pointer should start one node behind.
        head = ListNode(0,head) #Dummy start point
        second = head
        first = head.next
        while first:
            print(first.val,second.val)
            for i in range(k-1):
                if first:
                    first = first.next
                else:
                    break
            if first==None:
                break
            # now we have first pointer as tail
            # second pointer as head of window
            # we need a function which takes head and tail pointer
            # reverses the list and returns windowHead and windowTail
            # windowTail can be used to traverse further
            # first = windowTail.next, second = windowTail
            windowTail = first
            first = first.next
            windowTail.next = None
            windowHead = second.next
            windowHead,windowTail = self.reverseLL(windowHead,windowTail)
            second.next = windowHead
            second = windowTail
            windowTail.next = first
            # print(first.val,second.val)
        return head.next