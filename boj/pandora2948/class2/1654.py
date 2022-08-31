from sys import stdin

K, N = list(map(int, input().strip().split()))

cables = []

for _ in range(K) :
  cables.append(int(stdin.readline().strip()))

start, end = 1, max(cables)
conclusion = None

while start <= end :
  center = (start + end) // 2

  amount = sum(list(map(lambda ele : ele // center, cables)))

  if amount >= N :
    start = center + 1
    conclusion = center

  else :
    end = center - 1

print(conclusion)