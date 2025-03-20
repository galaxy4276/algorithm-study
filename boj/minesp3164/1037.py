count = int(input())
nums = list(map(int,input().split()))
nums.sort()
if count%2 == 1:
    middle_value = nums[len(nums) // 2]
    print(middle_value**2)
else:
    print(nums[0]*nums[-1])
