class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=101
        sell=0
        result=0
        for i in prices:
            if i<buy:
                buy=i
            else:
                sell=i
                result=max(sell-buy,result)
            # print(result)
        return result