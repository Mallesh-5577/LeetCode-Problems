class Solution(object):
    def maxProfit(self, prices):
        min_profit = float('inf')
        max_profit = 0

        for buy in prices:
            min_profit = min(min_profit,buy)
            max_profit = max(max_profit,buy-min_profit)

        return max_profit