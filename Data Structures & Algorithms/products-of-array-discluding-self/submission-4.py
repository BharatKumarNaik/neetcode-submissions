class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]*len(nums)
        suffix=[1]*len(nums)
        i,j=0,len(nums)-1
        prev_prefix=1
        prev_suffix=1
        while i<len(nums) and j>=0:
            prefix[i]*=prev_prefix
            suffix[j]*=prev_suffix
            prev_prefix*=nums[i]
            prev_suffix*=nums[j]
            i+=1
            j-=1
        res=[]
        for x,y in zip(prefix,suffix):
            res.append(x*y)
        return res