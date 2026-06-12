class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0,len(nums)-1
        result = nums[0]
        while l<r:
            mid = (l+r)//2
            if nums[l]<nums[r] and nums[mid]<nums[r]:
                result = min(result,nums[l])
                r = mid - 1
            elif nums[l]>nums[r] and nums[mid]>nums[r]:
                result = min(result,nums[r])
                l = mid+1
            elif nums[l]>nums[r] and nums[mid]<nums[r]:
                result = min(result,nums[mid])
                r = mid - 1
            elif nums[l]>nums[r] and nums[mid]>nums[r]:
                result = min(result,nums[r])
                l = mid + 1
        # print(mid)
        # result = min(nums[mid],result)
        return result
