class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
      oddNum = sorted(filter(lambda ele : ele % 2 != 0, nums))
      evenNum = sorted(filter(lambda ele : ele % 2 == 0, nums))
      

      nums.clear()
      
      for i in oddNum :
        evenNum.append(i)
      
      return evenNum
      
      
class Solution:
  def sortArrayByParity(self, nums: List[int]) -> List[int]:
    left = 0
    right = len(nums) - 1
  
    while left < right :
      if nums[left] % 2 == 0 :
        left += 1
        continue
      
      else :
        nums[left], nums[right] = nums[right], nums[left]
      right -= 1
    return nums