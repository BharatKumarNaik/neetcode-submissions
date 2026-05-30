class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums=sorted(list(set(nums)))
        if len(nums)==0:
            return 0
        result=1
        final=0
        for i in range(1,len(nums)):
            prev=nums[i-1]
            # print(nums[i],prev) 
            if nums[i]-prev==1:
                result+=1
            else:
                final=max(result,final)
                result=1
            # print(result)
        return max(final,result)