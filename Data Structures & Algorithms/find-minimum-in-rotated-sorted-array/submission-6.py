class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        result = nums[l]
        while l<=r:
            mid = (l+r)//2
            if nums[l]<nums[r]:
                result = min(result,nums[l])
                break
            elif nums[mid]<nums[l]:
                # move to left
                result = min(result,nums[mid])
                r = mid - 1
            else:
                # move to right
                result = min(result,nums[mid])
                l = mid + 1
        return result
