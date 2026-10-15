class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        bestPrice = 0
        buy = 100000000000          # something any real price can beat
        point = 0

        while point <= len(prices) - 1:

            # step 1: is today's price lower than buy?
            if prices[point] < buy:
                buy = prices[point]

            # step 2: if I sold today at today's price, is that profit
            # better than bestPrice?
            if prices[point] - buy > bestPrice:
                bestPrice = prices[point] - buy 

            point = point + 1            # move the pointer

        return bestPrice