class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        total = numBottles
        a = []
        nam = numBottles
        while (nam >= numExchange):
            total += nam / numExchange
            nam = int(nam / numExchange) + (nam % numExchange)

        return total