class Solution(object):
    def maxProfit(self, prices):
        if not prices or len(prices) < 2:
            return 0
        max_profit,min_price = 0,prices[0]
        
        for price in prices[1:]:
            max_profit = max(max_profit, price - min_price)
            min_price = min(min_price, price)
        
        return max_profit
