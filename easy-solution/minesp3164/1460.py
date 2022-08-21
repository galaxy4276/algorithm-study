class Solution(object):
    def canBeEqual(self, target, arr):
        target.sort()
        arr.sort()
        return target == arr
