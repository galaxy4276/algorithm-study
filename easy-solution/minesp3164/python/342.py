class Solution(object):
    def isPowerOfFour(self, n):
        j = 1
        while j < n:
            j *= 4
        if j == n:
            return True
        return False
        """
        :type n: int
        :rtype: bool
        """
