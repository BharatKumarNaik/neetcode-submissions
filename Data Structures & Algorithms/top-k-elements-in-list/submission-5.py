class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_bucket = [[] for i in range(len(nums)+1)]
        data={}
        for i in nums:
            if i not in data:
                data[i]=0
            data[i]+=1
        for num,cnt in data.items():
            freq_bucket[cnt].append(num)
        
        res=[]
        for i in range(len(freq_bucket)-1, 0,-1):
            for j in freq_bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res