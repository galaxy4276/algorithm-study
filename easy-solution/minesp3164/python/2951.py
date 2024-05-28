#Find the Peaks

class Solution(object):
    def findPeaks(self, m):
        i=1
        ans=[]
        while(i<len(m)-1):
            if m[i-1]<m[i] and m[i+1]<m[i]:
                ans.append(i)
                i+=1
            i+=1
        return ans