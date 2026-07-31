class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # sorting will also take nlogn time complexity
        # for kth largest/smallest we usually use heap
        # heap answer
        heap = [-i for i in nums]
        heapq.heapify(heap)
        while k!=1:
            heapq.heappop(heap)
            k-=1
        return -1*heapq.heappop(heap)