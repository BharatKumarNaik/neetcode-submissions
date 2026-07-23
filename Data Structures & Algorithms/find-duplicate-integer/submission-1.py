class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # list contains integers
        # can only contain values ranging between 0 to len(linked list)
        # only one element is duplicated find the element

        # Solution
        # They only contain +ve values.
        # so, when we traverse we will set the values to -ve.
        # if we encounter it again we will know by it's sign
        for num in nums:
            idx = abs(num)-1
            if nums[idx]<0: # -ve
                return abs(num)
            nums[idx]*=-1
        return -1