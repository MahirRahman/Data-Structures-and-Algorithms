class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        if len(prices) <= 1:
            return 0
        buy = -prices[0] - fee
        sell = 0
        # buy[0] = -prices[0]-fee
        # sell[0] = 0
        for i in range(1, len(prices)):
            buy = max(buy, sell - prices[i] - fee)
            sell = max(sell, buy + prices[i])
        return sell