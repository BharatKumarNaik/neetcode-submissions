class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # First we need to get the the frequency of occurences.
        data={}
        for i in nums:
            data[i] = data.get(i,0)+1
        heap=[(-y,x) for x,y in list(data.items())]
        heapq.heapify(heap)

        res=[]
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
