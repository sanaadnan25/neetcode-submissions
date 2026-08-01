class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxim  = []
        if len(prices) < 2:
            return 0
        i = 0
        while i < len(prices) - 1:
            price = prices[i+1:]
            curmax = max(price)
            maxim.append(curmax - prices[i])
            i+=1

        if max(maxim) < 0:
            return 0
        else:
            return max(maxim)
