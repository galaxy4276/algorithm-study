class Solution(object):
    def replaceElements(self, arr):
        maximum = -1
        for i in range(len(arr) - 1, -1, -1):
            arr[i], maximum = maximum, max(arr[i], maximum)
        return arr