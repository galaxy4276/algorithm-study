class Solution(object):
    def subtractProductAndSum(self, n):
        nlist = list(map(int,str(n)))
        sum = 0
        multiply = 1
        for i in range(len(nlist)):
            sum = sum + nlist[i]
            multiply = multiply * nlist[i]
        return multiply - sum
