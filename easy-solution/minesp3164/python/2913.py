#Subarrays Distinct Element Sum of Squares I
class Solution(object):
    def sumCounts(self, nums):
        sol = 0;
        for i in range(len(nums)):
            l = []
            h = set()
            for j in range(i,len(nums)):
                h.add(nums[j])
                d = len(h)
                d *= d
                sol += d
        return sol