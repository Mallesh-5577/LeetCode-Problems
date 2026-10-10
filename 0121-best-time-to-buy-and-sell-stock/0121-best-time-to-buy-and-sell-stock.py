class Solution(object):
    def maxProfit(self, prices):

        buy = float("inf")
        profit = 0

        for sell in prices:
            buy = min(buy,sell) 
            profit = max(profit,sell-buy)
            
        return profit