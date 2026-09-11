class Solution {
    public int maxProfit(int[] prices) {
        int min_price = Integer.MAX_VALUE;
        int max_profit = 0;
        for (int p : prices) {
            if (p < min_price) {
                min_price = p;
            }
            else {
                max_profit = Math.max(max_profit, p - min_price);
            }
        }
        return max_profit;
    }
}