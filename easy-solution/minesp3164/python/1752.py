# Check if Array Is Sorted and Rotated
class Solution(object):
    def check(self, nums):
        a = sorted(nums)
        for i in range(len(nums)):
            if nums[i:] + nums[:i] == a:
                return True
        return False
