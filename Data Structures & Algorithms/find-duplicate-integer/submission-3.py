class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # list contains integers
        # can only contain values ranging between 0 to len(linked list)
        # only one element is duplicated find the element

        # Solution
        # if n = 8
        # mid = 4, Check how many numbers are less or equal to 4
        # now check the lessOrEqual count against mid. It should be lessOrEqual to mid.
        # if there is no duplicates. in that case mid can be increased.
        # to make it faster we increase it in a binary search pattern. which is by moving low to mid +1
        # if it's greater then mid, means there exist some values between low to high.
        # which has duplicate values (remember mid here is representing like a window size, to which count of val <= mid should match)
        # now we know that there exist some value between low and mid which has duplicated values.
        # so we move high to mid
        # at the end, when high and low converges it will have the duplicated value.

        n = len(nums)
        low = 0
        high = n-1
        while low<high:
            mid = (low+high)//2
            valCount = sum(1 for num in nums if num<=mid)
            # valCount of only values which are less then mid
            if valCount<=mid:
                # No duplicate between low to mid
                low = mid+1
            else:
                # there exist a duplicate between low to mid
                high = mid
        return low