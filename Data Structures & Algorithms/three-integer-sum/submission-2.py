class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        # let's assume target as -nums[k] rather then 0
        nums.sort()
        # print(nums)
        k=0
        i=1
        j=len(nums)-1
        while k<len(nums)-2:
            if k>0 and nums[k]==nums[k-1]:
                k+=1
                continue
            i=k+1
            j=len(nums)-1
            while i<j:
                # print(nums[i],nums[j],nums[k])
                if nums[i]+nums[j]==-nums[k]:
                    result.append([nums[i],nums[j],nums[k]])
                    i+=1
                    j-=1
                    if nums[i]==nums[i-1]:
                        i+=1
                    if nums[j]==nums[j+1]:
                        j-=1
                elif nums[i]+nums[j]<-nums[k]:
                    i+=1
                    if nums[i]==nums[i-1]:
                        i+=1
                elif nums[i]+nums[j]>-nums[k]:
                    j-=1
                    if nums[j]==nums[j+1]:
                        j-=1
            k+=1
        return result