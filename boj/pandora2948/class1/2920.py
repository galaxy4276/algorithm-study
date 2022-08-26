nums = list(map(lambda ele: int(ele), input().strip().split()))

if sorted(nums) == nums :
  print("ascending")

elif sorted(nums, reverse = True) == nums :
  print("descending")

else :
  print("mixed")
