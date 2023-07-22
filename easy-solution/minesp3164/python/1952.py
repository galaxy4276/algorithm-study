# Three Divisors

class Solution(object):
    def isThree(self, n):
        count = 2
        for i in range(2,n//2 + 1):
            if n%i == 0:
                count += 1
            if count > 3:
                return 0
        if count != 3:
            return 0
        return 1