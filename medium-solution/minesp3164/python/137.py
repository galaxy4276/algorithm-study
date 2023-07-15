class Solution(object):
    def singleNumber(self, nums):
        if len(nums) == 1:
            return nums[0]
        answer = 0
        for i in range(len(nums)):
            if nums.count(nums[i]) == 1:
                return nums[i]