class Solution(object):
    def findGCD(self, nums):
        nums.sort()
        min = nums[0]
        max = nums[-1]
        list = []
        for i in range(1,max+1):
            if(min%i == 0 and max %i == 0):
                list.append(i)
        return list[-1]