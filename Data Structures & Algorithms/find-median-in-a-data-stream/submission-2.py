class MedianFinder:

    def __init__(self):
        self.smaller=[] # max heap
        self.larger=[]  # min heap

    def addNum(self, num: int) -> None:
        # check where num belongs larger or smaller
        if self.larger and self.larger[0]<num:
            heapq.heappush(self.larger,num)
        else:
            heapq.heappush(self.smaller,-1*num)
        
        # now need to check the length of the two list
        # as they should be approximately equal; either equal or 1 less then other
        if len(self.smaller)>len(self.larger)+1:
            val=-1*heapq.heappop(self.smaller)
            heapq.heappush(self.larger,val)
        if len(self.larger)>len(self.smaller)+1:
            val=heapq.heappop(self.larger)
            heapq.heappush(self.smaller,-1*val)

    def findMedian(self) -> float:
        s=len(self.smaller)
        l=len(self.larger)
        if (s+l)%2==0:
            val1=-1*self.smaller[0]
            val2=self.larger[0]
            mean=(val1+val2)/2
            return mean
        elif l>s:
            median=self.larger[0]
            return median
        else:
            median=-1*self.smaller[0]
            return median

        