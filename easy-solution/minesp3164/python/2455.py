class Solution(object):
    def averageValue(self, nums):
        ans = 0
        count = 0
        for i in nums:
            if i % 2 == 0 and i% 3 == 0:
                count += 1
                ans += i
        if count == 0:
            return 0
        return ans / count