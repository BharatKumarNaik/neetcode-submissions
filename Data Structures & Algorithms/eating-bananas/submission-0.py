import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # brute force
        if sum(piles)<=h:
            return 1
        k=2
        while k<=max(piles):
            oek=0 if k%2==0 else 1
            temp=0
            for i in piles:
                # ceil value of i,k
                # if i<=k:
                #     temp+=1
                #     continue
                # # print(f'k={k}')
                # oei=0 if i%2==0 else 1
                # if oei==oek:
                #     val=i//k
                # else:
                #     val=i//k+1
                # print(val)
                val=math.ceil(i/k)
                temp+=val
            print(temp,k)
            if temp<=h:
                return k
            k+=1


                