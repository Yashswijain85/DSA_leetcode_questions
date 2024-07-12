class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 1. First check if the list is empty or there is one element, if it is so, return 0 
        # 2. set max_profit = 0 and min_price as first element of an array
        # 3. update max_profit and min_price with: 
            #a. max_profit = max(max_profit, price-min_price)
            #b. min_price = min(price, min_price)
        # 4. return max_profit
        if not prices or len(prices) < 2:
            return 0
        max_profit, min_price = 0, prices[0]

        # Traverse from index 1 to last and update max_profit, min_price
        for price in prices[1:]:
            max_profit = max(max_profit, price-min_price)
            min_price = min(price, min_price)
        return max_profit
