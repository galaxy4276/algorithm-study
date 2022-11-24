class Solution(object):
    def reverse(self, x):
        s = str(abs(x))
        revers = int(s[::-1])

        if revers > 2147483647:
            return 0

        if x < 0:  revers *= -1
        return revers
