class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums.sort()
        for i in range(0,len(nums)-2):
            target=nums[i]
            j=i+1
            k=len(nums)-1
            while j<k:
                temp=nums[j]+nums[k]+target
                if temp==0:
                    if [target,nums[j],nums[k]] in result:
                        j+=1
                        continue
                    result.append([target,nums[j],nums[k]])
                    j+=1
                    k-=1
                elif temp<0:
                    j+=1
                else:
                    k-=1
        return result