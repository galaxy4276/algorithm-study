# 주몽

count = int(input())
ans = int(input())
list = list(map(int,input().split()))
cnt = 0
start,end = 0,count-1
list.sort()
while start != end:
  sum = list[start] + list[end]
  if sum < ans:
    start += 1
  elif sum > ans:
    end -= 1
  else:
    cnt += 1
    start += 1
print(cnt)