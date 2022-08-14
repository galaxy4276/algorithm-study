class Solution(object):
    def fib(self, n):
        first = 0
        second = 1
        answer = 0
        if n <= 2: return 1
        i = 0
        while i < n:
            answer = first + second
            first = second
            second = answer
        return answer