class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # If you are looking for better comment check previous commit
        heaviest = max(stones)
        bucket = [0]*(heaviest+1)
        for stone in stones:
            bucket[stone]+=1
        
        first,second = heaviest,heaviest
        while first>0:
            if bucket[first]%2==0:
                # if even gets cancelled out
                bucket[first]=0
                first-=1
            else:
                # if odd then we need to find the second heaviest
                j = min(first-1,second)
                # we are thinking there might be first-1 but still not sure
                while j>0 and bucket[j]==0:
                    j-=1
                    # we found the next non zero element from right side.
                    # which will be the freq of second highest stone
                if j==0:
                    # means there is no second element
                    return first
                second = j
                bucket[first]-=1
                bucket[second]-=1
                bucket[first-second]+=1
                first = max(first,first-second)
        return first                
