class Solution(object):
    def separateDigits(self, nums):
        b = []
        for i in nums:
            listn = list(map(int,str(i)))
            for j in listn:
                b.append(j)

        return b