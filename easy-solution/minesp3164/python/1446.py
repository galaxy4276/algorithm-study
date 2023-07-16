class Solution(object):
    def maxPower(self, s):
        maxcount = 1
        i,j = 1,0
        while j< len(s)-1:
            if s[j] == s[j+1]:
                i += 1
            else:
                i = 1
            maxcount = max(maxcount, i)
            j+=1
        return maxcount