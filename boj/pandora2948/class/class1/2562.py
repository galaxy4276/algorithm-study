from sys import stdin

list = []

for _ in range(9) :
  list.append(int(stdin.readline().strip()))

print(max(list))
print(list.index(max(list)) + 1)