class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count={}
        for task in tasks:
            if task not in count:
                count[task]=0
            count[task]+=1
        
        maxHeap=[-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time=0
        q=deque() # [-count,idleTime]

        while maxHeap or q:
            time+=1
            if maxHeap:
                cnt=1+heapq.heappop(maxHeap)
                if cnt!=0:
                    q.append([cnt,time+n])
            if q and q[0][1]==time:
                cnt=q.popleft()[0]
                heapq.heappush(maxHeap,cnt)
        return time
