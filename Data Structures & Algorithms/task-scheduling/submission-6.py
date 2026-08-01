class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # ["X","X","Y","Y"] n=2
        # [2,2]
        # pop max element and increment the counter
        # reduce it to 1. now this remaning 1 should wait for 2 unit of time
        # so add it to a waiting queue and mention what time it can enter the processing queue, which would be time+n
        # every iteration check top of queue (which will be the first/earliest push) if it's idle time is less then time then push it to processing queue which is actually a heap. else just look for next element in the processing queue(heap)
        # and process it, if that processing queue is empty but waiting queue is not then CPU will be idle for 1unit of time, till it's time breaches top of the waiting queue's idle time and after that it will be moved to processing queue and so on
        freqTask={}
        for task in tasks:
            if task not in freqTask:
                freqTask[task]=0
            freqTask[task]+=1
        processingQueue=[(-cnt,key) for key,cnt in freqTask.items()]
        heapq.heapify(processingQueue)
        # [-2,-2]
        waitingQueue=deque()
        res=[]
        time=0
        while processingQueue or waitingQueue:
            # print(processingQueue,time,waitingQueue)
            # print(res)
            if waitingQueue:
                if waitingQueue[0][2]<time:
                    # then cooldown time is over and it's ready for processing
                    freq,task,cooldownTime=waitingQueue.popleft()
                    heapq.heappush(processingQueue,(freq,task))
            if processingQueue:
                freq,task=heapq.heappop(processingQueue)
                freq=-1*freq #as we stored freq in -ve value to create maxHeap
                res.append(task)
                cooldownTime=time+n
                time+=1
                freq-=1
                if freq>0:
                    # send it to waitingQueue till it's cooldown ends
                    waitingQueue.append((-1*freq,task,cooldownTime))
            else:
                res.append('idle')
                time+=1
        print(res)
        return time



