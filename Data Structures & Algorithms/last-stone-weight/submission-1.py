class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we need to use heap
        # heapq is a min heap
        # so to get two heaviest stones, store the stones with -ve weight
        heap=[-i for i in stones]
        heapq.heapify(heap)
        while len(heap)>1:
            first = -1*heapq.heappop(heap)
            second = -1*heapq.heappop(heap)
            remains = -1*abs(second-first)
            heapq.heappush(heap,remains)
        return -1*heapq.heappop(heap)