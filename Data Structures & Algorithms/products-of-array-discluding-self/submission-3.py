class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[1]*len(nums)
        for i in range(len(nums)):
            result[:i]=list(map(lambda x:x*nums[i],result[:i]))
            result[i+1:]=list(map(lambda x:x*nums[i],result[i+1:]))
        return result