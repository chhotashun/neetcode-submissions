class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        profit = 0
        while right < len(prices):
            tmp = prices[right] - prices[left]
            if tmp < 0:
                left += 1
            else:
                right += 1
            profit = max(tmp, profit)
        return profit 
