from sys import stdin
from itertools import combinations

heights = list()

for _ in range(9) :
  heights.append(int(stdin.readline().strip()))

for i in combinations(heights, 7) :
  if sum(i) == 100 :
    for j in sorted(i) :
      print(j)
    break