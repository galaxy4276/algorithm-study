class Solution(object):
    def thirdMax(self, nums):
        setnums = sorted(set(nums))
        if len(setnums) >=3:
            return setnums[len(setnums) - 3]
        else:
            return setnums[-1]
"""
class Solution(object):
    def thirdMax(self, nums):
        nums.sort()
        setnums = list(set(nums))
        if len(setnums) >=3:
            return setnums[len(setnums) - 3]
        else:
            return setnums[-1]

"""


