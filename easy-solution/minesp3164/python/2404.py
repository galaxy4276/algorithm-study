#Most Frequent Even Element
class Solution(object):
    def mostFrequentEven(self, nums):
        nums.sort()
        nums = [num for num in nums if num %2 == 0]
        if not nums:
            return -1

        count = Counter(nums)

        for i in nums:
            if count[i] == max(count.values()):
                return i