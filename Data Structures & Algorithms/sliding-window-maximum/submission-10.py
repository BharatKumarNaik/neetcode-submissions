class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        leftmax = [float('-inf')]* n
        rightmax = [float('-inf')]*n

        leftmax[0] = nums[0]
        rightmax[n-1] = nums[n-1]

        for i in range(1,n):
            if i%k==0:
                leftmax[i]=nums[i]
            else:
                leftmax[i] = max(leftmax[i-1],nums[i])
            if (n-i-1) % k ==0:
                rightmax[n-i-1] = nums[n-i-1]
            else:
                rightmax[n-i-1] = max(rightmax[n-i],nums[n-i-1])
        
        output =[]
        for i in range(n-k+1):
            output.append(max(leftmax[i+k-1],rightmax[i]))
        return output
