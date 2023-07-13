class Solution(object):
    def repeatedNTimes(self, nums):
        count_nums = Counter(nums)
        for i in count_nums:
            if count_nums[i] == len(nums)/2:
                return i