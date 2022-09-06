class Solution(object):
    def moveZeroes(self, nums):
        count = 0
        for i in range(len(nums)):
            if(nums[i] != 0):
                nums[count] = nums[i]
                count+= 1
        for i in range(count,len(nums)):
            nums.insert(i, 0)
            nums.pop()


        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
