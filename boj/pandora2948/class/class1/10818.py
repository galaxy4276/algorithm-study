from sys import stdin

N = int(input())

nums = list(map(lambda ele : int(ele) ,stdin.readline().strip().split()))

print(min(nums), max(nums))