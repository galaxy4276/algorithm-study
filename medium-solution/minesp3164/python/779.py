class Solution(object):
    def kthGrammar(self, n, k):
        if n == 1:
            return 0
        else:
            if k % 2 == 0:
                return 1- self.kthGrammar(n-1,(k+1)//2)
            else:
                return self.kthGrammar(n-1,((k+1)//2))