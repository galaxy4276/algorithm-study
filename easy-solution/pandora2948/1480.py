class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        answer = []

        for i in range(1, len(nums) + 1):
          answer.append(sum(nums[0 : i]))

        return answer