class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin=1000
        mprofit=0
        for i in prices:
            mprofit=max(mprofit,i-lmin)
            lmin=min(lmin,i)
        return mprofit