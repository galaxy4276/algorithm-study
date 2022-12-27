from typing import List


# two pointer
def two_sum(nums: List[int], target: int) -> List[int]:
    left, right = 0, len(nums) - 1
    while left < right:
        plus = nums[left] + nums[right]
        if plus < target:
            left += 1
        elif plus > target:
            right -= 1
        else:
            return [left, right]


print(two_sum([2, 7, 11, 15], 9))


# 첫 번째 수를 뺀 결과 키 조회
# def two_sum(nums: List[int], target: int) -> List[int]:
#     nums_map = {}
#
#     for i, num in enumerate(nums):
#         print(f'i: {i} nums: {num}, map: {nums_map}')
#         if target - num in nums_map:
#             return [nums_map[target - num], i]
#         nums_map[num] = i


# in 을 이용한 탐색법
# def two_sum(nums: List[int], target: int) -> List[int]:
#     for i, n in enumerate(nums):
#         print(f'i: {i}, n: {n}')
#         complement = target - n
#         print(f'complement: {complement}')
#         print(f'nums[i+1:]: {nums[i + 1:]}')
#         if complement in nums[i + 1:]:
#             return [nums.index(n), nums[i + 1:].index(complement) + (i + 1)]

