class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        [1,1,2,8]
        [1,6,24,48]
        prev = 1
        p_list = [1]
        for i in range(len(nums)-1):
            prev = prev*nums[i]
            p_list.append(prev)
        
        r_list=[1]
        i=len(nums)-1
        prev=1
        while i>0:
            prev=prev*nums[i]
            r_list.append(prev)
            i-=1
        res=[]
        for i,j in zip(p_list,r_list[::-1]):
            res.append(i*j)
        return res

