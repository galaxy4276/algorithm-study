class Solution(object):
    def getMaximumGenerated(self, n):
        l1 = [0,1]
        if n == 2 or n == 1:
            return (1)
        elif n == 0:
            return (0)
        for i in range(1,n):
            l1.append(l1[i])
            if (i * 2) == n:
                break
            l1.append((l1[i]) + (l1[i+1]))
            if (((i * 2)+1) == n):
                break
        return (max(l1))