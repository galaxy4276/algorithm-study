class Solution(object):
    def findTheDifference(self, s, t):
        for i in t:
            if not i in s or s.count(i) != t.count(i):
                return i