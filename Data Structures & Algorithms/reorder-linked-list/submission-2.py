# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # let's try recursion
        # [1,2,3,4]
        def rec(root,cur):
            # first I need to reach the end and recursively
            # such that when rolled back we will get the element in reverse manner
            # then we just do reordering operation
            # need to perform this untill our root node == cur or root crosses cur
            if not cur:
                return root
            
            root = rec(root,cur.next)


            temp = None
            if root and (root == cur or root.next == cur):
                cur.next = None
            elif root:
                temp = root.next
                root.next = cur
                cur.next = temp
            return temp
        head = rec(head,head.next)
