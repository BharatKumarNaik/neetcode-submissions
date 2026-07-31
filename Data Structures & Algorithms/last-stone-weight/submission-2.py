class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # [2,7,4,1,8,1]
        # [0,1,1,0,1,0,0,1,1]
        heaviest = max(stones) #O(n)
        bucket = [0]*(heaviest+1)
        for stone in stones:
            bucket[stone]+=1
        # now bucket stores the freq of each weight of stones
        first,second = heaviest, heaviest
        while first>0:
            if bucket[first]%2==0:
                # if even then those stones will get cancelled out
                bucket[first]=0
                first-=1
            else:
                # if odd then we need to look for second highest weight
                j = min(first-1,second)
                while j>0 and bucket[j]==0:
                    j-=1
                    # find the next highest by traversing in reverse
                    # get's the next non zero freq
                if j==0:
                    # means there is no second value to be highest
                    return first
                second = j
                bucket[first]-=1
                bucket[second]-=1
                bucket[first-second]+=1
                # first and second gets cancelled out and first-second get's added
                first = max(second,first-second)
        return first