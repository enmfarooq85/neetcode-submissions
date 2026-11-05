class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bestBuy = prices[0]
        bestProfit = 0
        n = len(prices)

        for i in range(1, n):
            bestProfit = max(bestProfit, prices[i] - bestBuy)
            bestBuy = min(bestBuy, prices[i])

        return bestProfit
