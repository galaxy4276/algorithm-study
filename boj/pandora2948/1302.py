from sys import stdin

result = dict()

N = int(input())

for _ in range(N) :
  val = stdin.readline().strip()
  if not list(result.keys()).count(val) :
    result[val] = 1

  else :
    result[val] += 1

maxCount = max(result.values())

print(sorted(list(filter(lambda ele : ele[1] == maxCount, list(result.items()))))[0][0])
