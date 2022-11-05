class Solution {
    public int maxProfit(int[] prices, int fee) {
        int days = prices.length;
        if (days <= 1) return 0;
        int buy = - prices[0] - fee;
        int sell = 0;
        for (int i = 1; i < days; i++) {
            buy = Math.max(buy, sell - prices[i] - fee);
            sell = Math.max(sell, buy + prices[i]);
        }
        return sell;
    }
}