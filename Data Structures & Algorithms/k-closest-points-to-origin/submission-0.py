class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # Heap
        # calculate the distance for each co-ordinate
        # while calculating load it into a min heap
        # at the end just pop the top k elements from the heap
        heap=[]
        res=[]
        for x,y in points:
            distance = ((x**2)+(y**2))**(0.5)
            heapq.heappush(heap,(distance,(x,y)))
        while k!=0:
            k-=1
            d,xy=heapq.heappop(heap)
            res.append([xy[0],xy[1]])
        return res