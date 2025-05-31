class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0  # initialize final profit

        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:  # if today's price is more than yesterday's
                max_profit += prices[i] - prices[i - 1]  # we sell today, buy yesterday

        return max_profit

# Time complexity : O(n)
# Space complexity : O(1)
