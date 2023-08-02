# Permutations
class Solution(object):
  def permute(self, nums):
    return list(permutations(nums, len(nums)))
