class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # list contains integers
        # can only contain values ranging between 0 to len(linked list)
        # only one element is duplicated find the element

        # Solution
        # They only contain +ve values.
        # so, when we traverse we will set the values to -ve.
        # if we encounter it again we will know by it's sign
        # Idea is to treat value itself as index as all the values will range between 0 and n
        # so if there exists and duplicate, we will end up traversing to the same index.
        # since we are negating it when we visit the value, if it's a revisit; we will find the value as -ve.
        # that way we will know that index/value is duplicated. (note: not the nums[idx])
        for num in nums:
            idx = abs(num)-1
            if nums[idx]<0: # -ve
                return abs(num)
            nums[idx]*=-1
        return -1