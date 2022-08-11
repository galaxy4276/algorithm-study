class Solution(object):
    def sortArrayByParity(self, nums):
        i = 0
        count = 0
        while i <len(nums):
            if(nums[i] % 2 == 0):
                numbers = nums[count]
                nums[count] = nums[i]
                nums[i] = numbers
        return nums