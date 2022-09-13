class Solution:
  def removeDuplicates(self, nums: List[int]) -> int:
    alignNums = list(sorted(set(nums.copy())))
    nums.clear()
    for i in alignNums :
      nums.append(i)