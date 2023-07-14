class Solution(object):
    def differenceOfSum(self, nums):
        sum_element = sum(nums)
        sum_digits = 0
        a,b = 0,0
        for i in nums:
            if i >= 10:
                sum_i=sum([int(d) for d in str(i)])
                sum_digits+= sum_i
            else:
                sum_digits += i
        return sum_element - sum_digits