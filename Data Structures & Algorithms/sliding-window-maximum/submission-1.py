class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result=[]
        heap=[]
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            while heap[0][1]<=i-k: # Checks if the first element is out of bounded value or not
                heapq.heappop(heap) # remove the element untill top element belongs to the window
                #if some values still exist behind the min element which is outof bound of window ignore it
            if i>=k-1:
                result.append(-heap[0][0])
        return result