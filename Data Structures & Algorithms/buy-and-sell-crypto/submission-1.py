class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] > cheap:
                profit = prices[i] - cheap

                if profit > max_profit:
                    max_profit = profit
            else:
                cheap = prices[i]
        
        return max_profit