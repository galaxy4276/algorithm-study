# Count Distinct Numbers on Board

class Solution(object):
    def distinctIntegers(self, n):
        answer = 1
        for i in range(1,n):
            if n % i == 1:
                answer = i
        return answer