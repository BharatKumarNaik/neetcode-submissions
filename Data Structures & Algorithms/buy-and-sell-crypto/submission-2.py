class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lmin=1000
        result=0
        for i in prices:
            result=max(result,i-lmin)
            lmin=min(lmin,i)
        return result