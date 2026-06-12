class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0, len(nums)-1
        while l<=r:
            m = (l+r)//2
            if target == nums[m]:
                return m
            print(l,r,m)
            if nums[l]>nums[r]:
                # l - m and m - r is rotated as well or not we need to check
                if nums[l]<=nums[m]:
                    # left side is sorted
                    if target>=nums[l] and target<nums[m]:
                        r = m - 1
                    else:
                        l = m + 1
                else:
                    # right side is sorted
                    if target<=nums[r] and target > nums[m]:
                        l = m + 1
                    else:
                        r = m - 1
            else:
                # It's in sorted order
                print("sorted area")
                if target < nums[m]:
                    r = m - 1
                else:
                    l = m + 1
        return -1