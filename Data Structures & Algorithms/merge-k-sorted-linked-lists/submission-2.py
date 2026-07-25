# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class NodeWrapper:
    def __init__(self,node):
        self.node = node
    def __lt__(self,other):
        return self.node.val<other.node.val

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        '''Brute Force
        two pointer approach to find the min head node
        set lists[0] as first node.
        traverse second pointer from 1 till end.
        while traversing it needs to compare head of 2nd pointer to first pointer.
        if first is smaller move second else set first as second and move second
        after traversing all the way through, insert first node into new linkedlist
        and move first pointer's head node to nxt
        TimeComplexity: n = len(lists) -> O(n*(max(len(each nodes))))
        
        Optimal: using heap
        set each linked list node in the heap
        but heap can't track the object
        so we can use (val, node); but if val is same with other node then it will compare node with other node
        which will through error as it can't be compared (<).
        as a temp fix we can use (val,str(node),node)
        '''

        # if len(lists) ==0:
        #     return None

        # res = ListNode(0) # Base as dummy
        # cur = res
        # minHeap=[]
        # for head in lists:
        #     if head is not None:
        #         heapq.heappush(minHeap,(head.val,str(head),head))
        
        # while minHeap:
        #     val,strAdd,head = heapq.heappop(minHeap)
        #     cur.next = head
        #     head = head.next
        #     if head!=None:
        #         heapq.heappush(minHeap,(head.val,str(head),head))
        #     cur = cur.next
        
        # return res.next


        # This method works really well, but it's not proffesional way to work
        ''' we can use a NodeWrapper.
        heap requires a method to compare between two nodes/objects.
        and heapq performs < [LessThen] operation. With the help of wrapper we can
        let the heap know the comparision way.
        __lt__(self,other) this function helps it understand the same
        '''
        if len(lists)==0:
            return None
        
        res = ListNode(0) #Dummy Node
        cur = res
        minHeap=[]
        for head in lists:
            if head:
                heapq.heappush(minHeap,NodeWrapper(head))
        
        while minHeap:
            wrapper = heapq.heappop(minHeap)
            head = wrapper.node
            cur.next = head
            head = head.next
            if head:
                heapq.heappush(minHeap,NodeWrapper(head))
            cur = cur.next
        return res.next
