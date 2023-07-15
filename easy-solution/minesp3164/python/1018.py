class Solution(object):
    def prefixesDivBy5(self, nums):
        s = 0
        for i in range(len(nums)):
            s = s* 2 + nums[i]
            nums[i] = s % 5 == 0
        return nums