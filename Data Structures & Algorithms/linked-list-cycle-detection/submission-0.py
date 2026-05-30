# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        visited={}
        cur=head
        while cur!=None:
            if cur in visited.keys():
                return True
            visited[cur]=cur.val
            cur=cur.next
        return False