class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        n = len(prices)
        for i in range(n - 1):
            bruh = prices[i]
            pot = max(prices[i+1:])
            ans = max(ans, pot-bruh)
        return ans