from sys import stdin
N, X = list(map(int, stdin.readline().strip().split()))

A = list(map(int, stdin.readline().strip().split()))

for i in list(filter(lambda ele : ele < X, A)) :
  print(i, end=" ")
