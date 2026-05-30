class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        i=0
        result=[]
        while i<=len(nums)-k:
            j=i+k
            # print(nums[i:j])
            result.append(max(nums[i:j]))
            i+=1
        return result