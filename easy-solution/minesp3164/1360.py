from datetime import date
class Solution(object):
    def daysBetweenDates(self, date1, date2):
        date1 = list(map(int, date1.split('-')))
        date2 = list(map(int, date2.split('-')))
        start = date(date1[0],date1[1],date1[2])
        target = date(date2[0],date2[1],date2[2])
        return abs((start - target).days)