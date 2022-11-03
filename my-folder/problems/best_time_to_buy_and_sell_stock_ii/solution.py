class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        r = 1
        profit = 0
        while r < len(prices):
            if prices[r] > prices[r-1]:
                profit += prices[r] - prices[r-1]                
            r+=1
        return profit