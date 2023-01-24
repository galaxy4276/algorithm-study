from sys import stdin

n = int(stdin.readline().strip())

nums = [int(stdin.readline().strip()) for _ in range(n)]

if nums[1] - nums[0] == nums[2] - nums[1]:
    print(nums[-1] + nums[1] - nums[0])

else:
    print(nums[-1] * (nums[2] // nums[1]))
