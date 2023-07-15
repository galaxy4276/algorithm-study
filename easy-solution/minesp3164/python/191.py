class Solution(object):
    def hammingWeight(self, n):
        if n == 0:
            return 0
        if n & 1:
           return self.hammingWeight(n>>1) + 1
        else:
            return self.hammingWeight(n>>1)