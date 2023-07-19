class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        intervals.sort()
        ans=0
        prevEnd=intervals[0][1]
        for start,end in intervals[1:]:
            if start>=prevEnd:
                prevEnd=end

            else:
                ans+=1
                prevEnd=min(end,prevEnd)

        return ans           