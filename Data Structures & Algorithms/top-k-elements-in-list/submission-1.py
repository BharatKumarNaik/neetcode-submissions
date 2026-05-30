class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        data={}
        for i in nums:
            if i not in data:
                data[i]=0
            data[i]+=1
        temp=dict(sorted(data.items(),key=lambda item:item[1],reverse=True)[:k])
        return list(temp.keys())