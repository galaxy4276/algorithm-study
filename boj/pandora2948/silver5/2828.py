from sys import stdin

N, M = list(map(int, stdin.readline().strip().split()))

J = int(stdin.readline().strip())

bucketStart = 1
bucketEnd = M
count = 0
applePos = [int(stdin.readline().strip()) for _ in range(J)]

for position in applePos :
  while position < bucketStart or position > bucketEnd :
    if position > bucketEnd :
      bucketStart += 1
      bucketEnd += 1
      count += 1

    elif position < bucketStart :
      bucketStart -= 1
      bucketEnd -= 1
      count += 1

print(count)