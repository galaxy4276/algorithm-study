class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if len(timeSeries) == 0 :
            return 0
        fulltime = 0
        for i in range(len(timeSeries)-1):
                fulltime += min(timeSeries[i+1] - timeSeries[i] , duration)
        return fulltime + duration