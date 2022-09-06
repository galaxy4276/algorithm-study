class Solution(object):
    def isUgly(self, n):
     p = [2,3,5]
     for i in range(len(p)):
         while n% p[i] == 0  <n :
             n /= p[i]
     return n == 1