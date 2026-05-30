class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result=[0]*len(nums)
        i=0
        j=len(nums)-2
        postfix=1
        while i<len(nums):
            # prefix mul storing
            if i-1<0:
                result[i]=1
                i+=1
                continue
            result[i]=nums[i-1]*result[i-1]
            i+=1
        # print(result)
        while j>=-1:
            #postfix mul to result
            # print(postfix)
            result[j+1]=postfix*result[j+1]
            postfix*=nums[j+1]
            j-=1
        return result