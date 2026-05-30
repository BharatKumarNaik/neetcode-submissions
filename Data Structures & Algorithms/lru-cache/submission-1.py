class LRUCache:

    def __init__(self, capacity: int):
        self.cache={}
        self.capacity=capacity
        self.priority=1

    def get(self, key: int) -> int:
        # print('in get')
        # print(self.cache)
        if key in self.cache:
            temp=self.cache[key]
            m=max(list(map(lambda x:x[1],self.cache.values())))
            self.cache[key]=[temp[0],m+1]
            self.priority=m+2
            return self.cache[key][0]
        # print(self.cache)
        return -1

    def put(self, key: int, value: int) -> None:
        # print('in put')
        if key in self.cache or len(self.cache)<self.capacity:
            self.cache[key]=[value,self.priority]
            self.priority+=1
        else:
            items=list(self.cache.items())
            items.sort(key=lambda x:x[1][1])
            del(self.cache[items[0][0]])
            self.cache[key]=[value,self.priority]
            self.priority+=1
        # print(self.cache)
        

