class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        amount = 0
        
        for i in range(len(nums)) :
          if nums[i] ==0 :
            amount += 1
          else :
            continue
        
        for _ in range(amount) :
          nums.remove(0)
          nums.append(0)