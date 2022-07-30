class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        max_count = 0
        count = 0
        for i in range(len(nums)):
            if(nums[i] == 1):
                count = count + 1
            else:
                max_count = max(max_count, count)
                count = 0
        return max_count
