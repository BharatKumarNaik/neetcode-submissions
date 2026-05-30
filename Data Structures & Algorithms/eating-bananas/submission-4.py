import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # optimal O(log(max)*n)
        # brute force O(max*n)
        l,r=1,max(piles)
        res=r
        while l<=r:
            k=(l+r)//2
            hours=0
            for i in piles:
                hours+=math.ceil(i/k)
            if hours <=h:
                res=min(res,k)
                r=k-1
            else:
                l=k+1
        return res


                