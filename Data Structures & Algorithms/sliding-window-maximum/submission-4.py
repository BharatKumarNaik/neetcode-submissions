class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        l,r = 0,k-1
        while l<=r and r<len(nums):
            result.append(max(nums[l:r+1]))
            r+=1
            l+=1
        return result