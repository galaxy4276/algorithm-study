class Solution(object):
    def heightChecker(self, heights):
        sortedheights = []
        for i in range(len(heights)):
            sortedheights.append(heights[i])
        count = 0
        heights.sort()
        for i in range(len(heights)):
            if(sortedheights[i] != heights[i]):
                count += 1
        return count
        """
        :type heights: List[int]
        :rtype: int
        """
