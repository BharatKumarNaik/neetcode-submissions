class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        i=0
        while i<len(nums):
            if i-1<0:
                result[i]=1
                i+=1
                continue
            result[i]=result[i-1]*nums[i-1]
            i+=1
        j=len(nums)-2
        postfix=1
        print(result)
        while j>=0:
            postfix *=nums[j+1]
            result[j]*=postfix
            j-=1
        return result

