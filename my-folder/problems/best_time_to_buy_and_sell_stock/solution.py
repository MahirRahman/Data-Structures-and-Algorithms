class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest = float('inf')
        highest  = 0
        for i in range(len(prices)):
            highest = max(highest, prices[i] - lowest)
            if prices[i] < lowest:
                lowest=prices[i]
        return highest