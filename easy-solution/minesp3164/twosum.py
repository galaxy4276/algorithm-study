class Solution(object):
    def twoSum(self, nums, target):
      answer = []
      for i in range (len(nums)):
          for j in range(len(nums)):
             if(i != j):
                if(nums[i] + nums[j] == target):
                   answer.append(i)
                   answer.append(j)
                   return answer
      