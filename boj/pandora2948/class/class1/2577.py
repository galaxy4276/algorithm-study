from sys import stdin

list1 = []
dict1 = {}

for _ in range(3) :
  list1.append(int(stdin.readline().strip()))

for i in range(10) :
  dict1[i] = 0

mult = list(str(list1[0] * list1[1] * list1[2]))

set1 = set(mult)

for i in set1 :
  dict1[int(i)] = mult.count(i)

for i in range(10) :
  print(dict1[i])