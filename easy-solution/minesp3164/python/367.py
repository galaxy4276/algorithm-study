class Solution(object):
    def isPerfectSquare(self, num):
        sqrtint = num ** 0.5
        return sqrtint == int(sqrtint)