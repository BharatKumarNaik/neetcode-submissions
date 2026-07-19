# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        def rec(root,cur):
            # first I need to reach the end and recursively
            # such that when rolled back we will get the element in reverse manner
            # then we just do reordering operation
            # need to perform this untill our root node == cur or root crosses cur
            if not cur: #None
                return root

            root = rec(root,cur.next)
            temp=None
            if root and (root==cur or root.next==cur):
                # means root has reached or crossed cur
                # depending on the linked list size
                # if oddd crossed else reached
                cur.next = None
            elif root:
                temp=root.next
                root.next = cur
                cur.next = temp
            return temp # At the end it returns none
        rec(head,head.next)