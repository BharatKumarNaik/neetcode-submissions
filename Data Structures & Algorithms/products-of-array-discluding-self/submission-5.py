class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[1]
        postfix=[1]
        i=0
        j=len(nums)-1
        while i<len(nums) and j>=0:
            t_pre = prefix[-1]
            prefix.append(t_pre*nums[i])
            t_pos = postfix[-1]
            postfix.append(t_pos*nums[j])
            i+=1
            j-=1
        # O(n)
        i=0
        j=len(nums)-1
        res=[]
        while i<len(nums) and j>=0:
            res.append(postfix[j] * prefix[i])
            i+=1
            j-=1
        # O(n)
        return res
