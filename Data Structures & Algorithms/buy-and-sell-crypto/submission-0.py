class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        bestProfit = 0

        for i in range(n):
            for j in range(i + 1, n):
                bestProfit = max(bestProfit, prices[j] - prices[i])

        return bestProfit
