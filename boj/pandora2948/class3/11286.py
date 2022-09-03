from sys import stdin
import heapq

hq = list()

for _ in range(int(stdin.readline().strip())) :
  val = int(stdin.readline().strip())

  if val == 0 :
    if not hq :
      print("0")

    else :
      print(heapq.heappop(hq)[1])

  else :
    heapq.heappush(hq, (abs(val), val))
