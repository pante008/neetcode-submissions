class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        if not prices:
            return 0
        minp=prices[0]
        max_profit = 0
        for p in prices[1:]:
            profit = p-minp
            max_profit = max(profit, max_profit)
            minp=min(minp,p)
        return max_profit
        