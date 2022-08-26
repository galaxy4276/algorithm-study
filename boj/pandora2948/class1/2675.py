from sys import stdin

T = int(input())

for _ in range(T) :
  R, S = stdin.readline().strip().split()

  for char in S :
    print(char * int(R), end="")

  print()