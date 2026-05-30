class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r=0,len(nums)-1
        while l<=r:
            print(nums[l:r+1])
            m=(l+r)//2
            if nums[m]==target:
                return m
            elif nums[l]<=nums[m]:
                # it's in left sorted array
                if target < nums[l]:
                    l=m+1
                elif target>=nums[l] and target<nums[m]:
                    r=m-1
                elif target>nums[m]:
                    l=m+1
            else:
                # m is in right sorted array
                if target<nums[m]:
                    r=m-1
                elif target>nums[m] and target>=nums[l]:
                    r=m-1
                elif target>nums[m] and target<nums[l]:
                    l=m+1
        return -1