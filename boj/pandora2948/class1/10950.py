from sys import stdin

T = int(input())

for _ in range(T) :
  print(sum(list(map(lambda ele : int(ele), stdin.readline().strip().split()))))