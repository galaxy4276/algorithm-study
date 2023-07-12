class Solution(object):
    def maxProfit(self, prices):
        maximum = 0
        minimum = sys.maxsize

        for price in prices:
            minimum = min(minimum, price)
            maximum = max(maximum, price - minimum)

        return maximum