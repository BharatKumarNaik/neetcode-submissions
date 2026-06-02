class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Using Heap
        heap = []
        output = []
        for i in range(len(nums)):
            heapq.heappush(heap,(-nums[i],i))
            # heapq is a min-heap, to behave it as max-heap we just negate the value
            if len(heap)>=k:
                # from now on we have to store the maxvalue.
                while heap[0][1] <= i-k:
                    heapq.heappop(heap)
                    # if the max element's index is not in the window range [i:k]
                    # we delete them
                output.append(-heap[0][0]) # which is the max element
                # negating it back again
        return output

'''
        Note:
        - Every element is pushed into the heap along with its index.
        - Once the first window of size k is formed, we start collecting results.
        - The heap may contain elements that are no longer inside the current window.
        - Before taking the maximum, remove all stale elements from the top of the heap
          (elements whose index falls outside the current window).
        - After removing stale elements, the heap's top element represents the maximum
          value within the current sliding window.
'''