class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # slow=0
        # max_price = 0
        # for fast in range(len(prices)):
        #     diff = prices[fast] - prices[slow]
        #     if prices[slow]<prices[fast]:
        #         max_price = max(diff,max_price)
        #     else:
        #         slow=fast
        # return max_price
        minPurchase=float('inf')
        maxProfit=0
        for price in prices:
            if price < minPurchase:
                minPurchase = price
            curProfit = price - minPurchase
            if curProfit > maxProfit:
                maxProfit = curProfit
           
        return maxProfit
        
        
        
        
        
        # min_price = float('inf')
        # min_index = -1
        # while slow < len(prices):
        #     if prices[slow] < min_price:
        #         min_price = prices[slow]
        #         min_index = slow
        #     slow+=1
        # max_price = float('-inf')
        # max_index = -1
        # while slow < min_index:
        #     if prices[slow] > max_price:
        #         max_index = slow
        #         max_price = prices[slow]
        #     slow+=1
        # return fast-slow