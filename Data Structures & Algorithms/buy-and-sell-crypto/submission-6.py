class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 1000
        profit = 0
        for i in prices:
            lowest = min(i,lowest)
            profit = max(profit,i-lowest)
        return profit