class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        output = []
        l,r = 0,0
        while l<=r and r<len(nums):
            # print(1,dq)
            while dq and nums[dq[-1]]<nums[r]:
                dq.pop()
            dq.append(r)
            # print(2,dq)
            if l>dq[0]:
                dq.popleft()
            
            # print(3,dq)
            if (r+1) >=k:
                output.append(nums[dq[0]])
                l+=1
            r+=1
        return output