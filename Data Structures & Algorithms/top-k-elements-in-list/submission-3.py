class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data={}
        for i in nums:
            if i not in data:
                data[i]=0
            data[i]+=1
        
        heap=[]
        for i in data:
            heapq.heappush(heap,[data[i],i])
            if len(heap)>k:
                heapq.heappop(heap)

        res=[]
        i=0
        while i<k:
            res.append(heapq.heappop(heap)[1])
            i+=1
        return res