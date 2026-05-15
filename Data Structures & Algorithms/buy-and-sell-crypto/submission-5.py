class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1 
        max_profit = 0
        while (right < len(prices)):
            temp = prices[right] - prices[left]
            print(temp)
            if (temp >= 0):
                max_profit = max(max_profit, temp)
                right += 1
            else:
                left += 1
                right = left + 1
            print(max_profit)
        return max_profit 
            
            