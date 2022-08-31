from sys import stdin

N = int(input())

strings = list()

for _ in range(N) :
  strings.append(stdin.readline().strip())

sortedStrings = sorted(sorted(set(strings)), key=len)

for i in sortedStrings :
  print(i)