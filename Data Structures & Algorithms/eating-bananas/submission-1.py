import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force
        if sum(piles)<=h:
            return 1
        k=2
        while k<=max(piles):
            temp=0
            for i in piles:
                val=math.ceil(i/k)
                temp+=val
            print(temp,k)
            if temp<=h:
                return k
            k+=1


                