class Solution(object):
    def kthFactor(self, n, k):
        n_list = []

        for i in range(1,n+1):
            if(n%i == 0):
                 n_list.append(i)
        if k > len(n_list):
            return -1
        return n_list[k-1]