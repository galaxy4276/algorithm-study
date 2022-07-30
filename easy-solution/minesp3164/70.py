class Solution(object):
    def climbStairs(self, n):
        previewnum1 = 1
        previewnum2 = 2
        after =  0
        if n == 1:
            return 1
        if n == 2:
            return 2
        if n >= 3:
            for i in range(n - 2):
                after = previewnum1 + previewnum2
                previewnum1 = previewnum2
                previewnum2 = after
        return after

