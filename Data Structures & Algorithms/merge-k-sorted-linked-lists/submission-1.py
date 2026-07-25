# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        # Brute Force
        # two pointer approach to find the min head node
        # set lists[0] as first node.
        # traverse second pointer from 1 till end.
        # while traversing it needs to compare head of 2nd pointer to first pointer.
        # if first is smaller move second else set first as second and move second
        # after traversing all the way through, insert first node into new linkedlist
        # and move first pointer's head node to nxt
        # TimeComplexity: n = len(lists) -> O(n*(max(len(each nodes))))
        
        # Optimal: using heap
        # set each linked list node in the heap
        # but heap can't track the object
        # so we can use (val, node); but if val is same with other node then it will compare node with other node
        # which will through error as it can't be compared (<).
        # as a temp fix we can use (val,str(node),node)
        if len(lists) ==0:
            return None

        res = ListNode(0) # Base as dummy
        cur = res
        minHeap=[]
        for head in lists:
            if head is not None:
                heapq.heappush(minHeap,(head.val,str(head),head))
        
        while minHeap:
            val,strAdd,head = heapq.heappop(minHeap)
            cur.next = head
            head = head.next
            if head!=None:
                heapq.heappush(minHeap,(head.val,str(head),head))
            cur = cur.next
        
        return res.next