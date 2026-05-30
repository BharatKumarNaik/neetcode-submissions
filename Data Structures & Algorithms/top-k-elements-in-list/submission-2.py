class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data={}
        for i in nums:
            if i not in data:
                data[i]=0
            data[i]+=1
        values=list(data.items())
        return list(map(lambda x: x[0],sorted(values,key=lambda x:x[1])[::-1]))[:k]
