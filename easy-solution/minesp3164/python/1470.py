class Solution(object):
    def shuffle(self, nums, n):
        result = []
        for i in range(n):
            result.append(nums[i])
            result.append(nums[n+i])
        return result