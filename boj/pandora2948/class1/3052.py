from sys import stdin

list1 = []

for _ in range(10) :
  list1.append(int(stdin.readline().strip()) % 42)

set1 = set(list1)

print(len(set1))