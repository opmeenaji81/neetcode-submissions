class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheap = prices[0]
        prof = []
        for i in range(len(prices)):
            if prices[i] > cheap:
                profit = prices[i] - cheap
                prof.append(profit)
            else:
                cheap = prices[i]
        
        if len(prof)>0:
            return max(prof)
        else:
            return 0