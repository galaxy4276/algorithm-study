class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        return sum(i in jewels for i in stones)