class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = 1000
        profit = []
        for i in prices:
            lowest = min(lowest,i)
            profit.append(i-lowest)
        return max(profit)