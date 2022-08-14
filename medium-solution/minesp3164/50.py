mysol..
class Solution:
    def myPow(self, x, n):
        return x**n
이렇게 푸는게 아닌걸 알지만..


""" disscuss
    class Solution:
        def myPow(self, x, n):
            if not n:
                return 1
            if n < 0:
                return 1 / self.myPow(x, -n)
            if n % 2:
                return x * self.myPow(x, n - 1)
            return self.myPow(x * x, n / 2)
"""
