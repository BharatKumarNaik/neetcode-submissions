class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Deque Method: But will be using list
        deque=[] # Double ended queue
        result=[]
        for i in range(len(nums)):
            #If we found the new element which is higher then we need to pop untill we find lower
            while deque and nums[deque[-1]]<nums[i]:
                deque.pop()
            deque.append(i)

            # we also have to remove the elements which are outof window
            while deque and deque[0]<= i-k:
                deque.pop(0) # pop from the front
            # now we will have the max element of the window in the left side
            if i>=k-1:
                result.append(nums[deque[0]])
        return result


