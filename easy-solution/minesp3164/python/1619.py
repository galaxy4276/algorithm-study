class Solution(object):
    def trimMean(self, arr):
        k = len(arr) / 20
        return sum(sorted(arr)[k:-k]) / (k * 18.)