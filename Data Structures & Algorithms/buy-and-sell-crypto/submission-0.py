class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Brute force
        mreturn=0
        i=0
        while i<len(prices)-1:
            j=i+1
            while j<len(prices):
                mreturn=max(mreturn,prices[j]-prices[i])
                j+=1
                # print(mreturn)
            i+=1
        return mreturn