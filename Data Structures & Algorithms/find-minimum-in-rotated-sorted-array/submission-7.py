class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m]<nums[r]:
                # then it must be on left including middle
                r=m
            else:
                # we felt the rotation and m>r then it must be on right
                l = m + 1
        return nums[l]