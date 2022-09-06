class Solution(object):
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(nums)):
            digit = len(str(nums[i]))
            if digit % 2 == 0:
                count = count + 1
        return count