class Solution(object):
    def canBeIncreasing(self, nums):
        preview = 0
        bools = False
        nums.append(sys.maxsize)
        i = 0
        n = len(nums) - 1
        while i < n :
            if preview < nums[i] < nums[i + 1]:
                preview = nums[i]
            else:
                if bools:
                    return False
                bools = True
                if nums[i+1] <= preview:
                    preview = nums[i]
                    i += 1
            i += 1
        return True
        """
        :type nums: List[int]
        :rtype: bool
        """