class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        profit = 0
        while (sell < len(prices)):
            max_profit = prices[sell] - prices[buy]
            if (max_profit > profit):
                profit = max_profit 
            if (max_profit < 0):
                buy += 1
            else:
                sell += 1
        return profit