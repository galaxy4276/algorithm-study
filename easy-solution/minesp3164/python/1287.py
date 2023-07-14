import collections


class Solution(object):
    def findSpecialInteger(self, arr):
        collect = collections.Counter(arr)
        for i in collect:
            if collect[i] > len(arr)//4:
                return i