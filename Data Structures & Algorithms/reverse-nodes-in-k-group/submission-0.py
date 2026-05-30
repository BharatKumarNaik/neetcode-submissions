# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # find k_tail
        # if k_tail not null and k_arb==0
        # reverse sub string between k_head and k_tail
        k_head=head
        first=0
        res=head
        prev=None
        while k_head!=None:
            k_tail=k_head
            k_arb=k-1
            while k_arb!=0:
                if k_tail==None:
                    return res
                k_tail=k_tail.next
                k_arb-=1
            if first==0:
                res=k_tail
                first=1
            # now k_tail is at the end of the k sub list
            if prev!=None and k_tail!=None:
                prev.next=k_tail
            if k_tail==None:
                return res
            k_tail=k_tail.next
            end=k_tail
            # print(k_tail.val if k_tail!=None else None)
            # print(prev.val if prev!=None else None)
            prev=k_head
            while k_head!=end:
                # print(k_head.val,k_tail.val)
                nxt=k_head.next
                k_head.next=k_tail
                k_tail=k_head
                k_head=nxt
        return res
            

                
                