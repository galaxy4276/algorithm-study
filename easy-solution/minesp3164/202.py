# saw solution
class Solution(object):
    def isHappy(self, n):
        def next(number):
            add = 0
            while number > 0 :
                number , digits=divmod(number, 10)
                add += digits ** 2
            return add
        slow = n
        fast =next(n)
        while fast != 1 and slow != fast:
            slow = next(slow)
            fast = next(next(fast))
        return  fast == 1

        """
        :type n: int
        :rtype: bool
        """
