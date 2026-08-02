class MedianFinder:

    def __init__(self):
        self.data=[]
        self.n=0

    def addNum(self, num: int) -> None:
        heapq.heappush(self.data,num)
        self.n+=1

    def findMedian(self) -> float:
        self.data.sort()
        if self.n%2==0:
            m1=(self.n//2)-1
            m2=m1+1
            mid=(self.data[m1]+self.data[m2])/2
        else:
            m=(self.n//2)
            mid=self.data[m]/1.0
        return mid
        