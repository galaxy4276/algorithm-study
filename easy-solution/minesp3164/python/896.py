class Solution(object):
    def isMonotonic(self, nums):
        increase = True
        decrease = True
        for i in range(len(nums)-1):
            if nums[i] < nums[i+1]:
                decrease = False
            if nums[i] > nums[i+1]:
                increase = False
        return increase or decrease
