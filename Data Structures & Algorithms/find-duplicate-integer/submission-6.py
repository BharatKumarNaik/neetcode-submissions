class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # list contains integers
        # can only contain values ranging between 0 to len(linked list)
        # only one element is duplicated find the element

        # Solution
        # Slow and fast pointer (Floyd's Fast & Slow technique)
        # this method is used to find the mid, also to find the cycle in cyclic list/graph
        # slow pointer will move considering nums's value as a index.
        # and fast pointer will move 2 index ahead considering nums's value as index as well.
        # when we encounter duplicate index, that part can be considered as a loop.
        # both slow and fast pointer will eventually converge at that point.
        slow = nums[0]
        fast = nums[0]

        # Phase 1: Find intersection point
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # if it was a 2 node cycle it's easier to declare slow/fast as the duplicate
        # but if there exist >2 nodes, we need to find the entrance of the cycle
        # Phase 2: Find cycle entrance
        slow2 = nums[0]

        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]

        return slow