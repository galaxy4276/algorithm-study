"""
   2022-07-16 galaxy4276 Code Review
   * 단순한 알고리즘 문제이기 때문에 answer = [] 리스트형 메모리를 저장해둘 필요가 없습니다.
      - answer = [] 요소 제거 가능
   * 2중 for문에서 i != j 로 같은 요소를 체크하는 것 보다 range(i + 1, ..) 으로
    수정하는것이 메모리 상 더 효율적입니다.
      -  if (i != j) 요소 제거 가능
   * 리스트 자료형은 리터럴 표현식으로 반환가능합니다.
      - return answer -> return [i, j]
"""

class Solution(object):
    def twoSum(self, nums, target):
      for i in range (len(nums)):
          for j in range(i + 1,len(nums)):
            if(nums[i] + nums[j] == target):
               return [i, j]
      